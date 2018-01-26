__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from  src import modules
import pickle
import os
from conf import setting
dic2 = {'teacher_name':'',"student_name":'',"grade":'',"class":''}
def  show_choice():
    msg = '''
    '1' 选择班级,查看学生列表
    '2' 成绩管理
    '''
    print(msg)
def dic():
    dic1 = {
        '1': choice_class,
        '2':change_grade,
    }
    return dic1
def choice_class():
    class_l = modules.Classes.get_info_all()
    print(class_l)
    print(modules.Classes.get_info_all())
    res2 = []
    for obj2 in class_l:
        res = []
        # if obj2.course_to_teacher == dic2["teacher_name"]:
        res.append(obj2.name)
        res.append(obj2.course_to_school)
        # res.append(obj2.school_nid)
        res2.append(res)
        res = []

    for k,a in enumerate(res2):
        print(k,a)
    b = int( input("请选择班级(输入编号):"))
    class_name = res2[b]
    dic2["class"] = class_name
    student_l = modules.Student.get_info_all()
    for obj in student_l:
        if dic2['teacher_name']  in obj.classes_nid.get_obj_by_uuid().course_to_school:
            print(obj.name)


    # 选择班级
    pass
def change_grade():
    student_n = input("学生名字")
    classes_n = input("班级名字")
    course_n = input("课程名字")
    count = input("学生成绩")
    s1 = modules.Grade(student_n, classes_n, course_n, count)
    if len(modules.Grade.get_info_all()) == 0 :
        # s1 = modules.Grade(student_n, classes_n, course_n, count)  # ,student_name,classes_name,course_name,count
        s1.save()
    else:
        grade_l = modules.Grade.get_info_all()
        for obj in grade_l:
            if student_n == obj.student_name and classes_n == obj.classes_name:
                print(obj.count)
                count_change = input("成绩更改为：")
                s1.count = count_change
                path = setting.GRADE_PATH
                pickle.dump(open("%s\%s" % (path,obj.nid.uuid), 'wb'))





def login():
    name = input("你的名字")
    dic2['teacher_name'] = name
    passwd = input("你的密码")

    show_choice()
    choice = input("你想干什么")
    dic()[choice]()





