__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from src import modules
from src.service import admin_service
import json
from conf import setting
import pickle

def show_choice():
    msg = '''
        1:"注册，并选择班级等信息",
        2:"缴费",
        3."成绩查询"
    '''
    print(msg)
def  choose():
    dic= {
        "1":sign_in ,
        "2":pay,
        "3":grade_m,
    }
    return dic


res = []
# dic_create_student = {}
def sign_in():
    dic_create_student = admin_service.create_student()
    # {'status': status, 'error': error, 'data': data, "name": student_name, "age": student_age, "tuition": '',
    #  "class_name": class_obj, 'tuition_status': 'Flase'}
    pickle.dump(dic_create_student,open("%s\student_message" %setting.BASE_PATH,'wb'))
    if dic_create_student.get('status') == True:
        print(dic_create_student['data'])
        print("下方是你的注册信息")

        print("姓名:%s ,年龄:%s,目前缴费状况%s,是否完成缴费%s" % (dic_create_student["name"],\
             dic_create_student["age"],dic_create_student["tuition"],dic_create_student['tuition_status'],))
        res.append(dic_create_student["class_name"])
    else:print(dic_create_student['error'])
    return dic_create_student


def  pay():
    # dic_create_student = admin_service.create_student()
    a = pickle.load(open('%s\student_message'%setting.BASE_PATH,'rb'))
    # class_obj = a["class_name"]
    print("你需要付%s" % a["class_name"].tuition)
    pay_c = input("输入你的缴费金额:")
    if  float(pay_c) - float(a["class_name"].tuition) == '0':
        a["tuition_status"] = False
        print("缴费完成")
    else:
        a["class_name"].tuition = str(float(a["class_name"].tuition) - float(pay_c))
        pickle.dump(a, open("%s\student_message" % setting.BASE_PATH, 'wb'))
        print("你还需交费",a["class_name"].tuitionstu)

def grade_m():
    #查看成绩
     if len(modules.Grade.get_info_all()) == 0:
         print("还没有录入成绩，请等待老师批改")
     grade_l = modules.Grade.get_info_all()
     for obj  in  grade_l:
         print("学生名字：%s ,成绩：%s" %(obj.student_name,obj.count))


def login():
    # show_choice()
    while True:
        show_choice()
        choice = input("你想做什么:(请输入编号)")
        if choice not in choose().keys():
            print("请重新输入")
            continue
        ret = choose()[choice]()  # ret = 函数运行的结果

        if ret:
            if ret['status']:
                print(ret['data'])
            else:
                print(ret['error'])
# 学员视图， 可以注册， 交学费， 选择班级，
# 1.验证
