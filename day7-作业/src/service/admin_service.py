__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from src import modules
def show_choice():
    msg = '''
        0:'选项',
        1:'创建学校'
        2:'查看学校'
        3:'创建老师'
        4:'查看老师'
        5:'创建课程'
        6:'查看课程'
        7:'关联老师与课程
        8:'创建班级'
        9:'查看班级'
        10:'创建学生'
        11:'查看学生'
        12:'退出'
        '''
    print(msg)

def create_school():
    try:
        name = input("学校的名称：")
        addr = input("学校的地址")
        res2 = []
        print("bbbbbbbbbbbbbb",modules.School.get_info_all())
        for obj  in  modules.School.get_info_all():
            res = []
            res.append(obj.name)
            res.append(obj.addr)
            res2.append(res)
            res = []
        if [name,addr] in res2:
            raise Exception('\033[43;1m[%s] [%s]校区 已经存在,不可重复创建\033[0m' % (name, addr))


        s1 = modules.School(name,addr)
        s1.save()
        status = True
        error = ''
        data = ('\033[33;1m 创建成功\033[0m' )
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_school():
    # print('学校 %s，地点 %s'% (modules.School.get_info_all().name,modules.School.get_info_all().addr))
    for k,obj in enumerate(modules.School.get_info_all()):
        print(k,"名字",obj.name,"地点",obj.addr)


def create_teacher():

    try:
        name = input("老师名称：")
        level = input("老师级别：")
        school_nid = input("学校是(请输入编号)：")
        res2 = []
        for obj  in  modules.Teacher.get_info_all():

            res = []
            res.append(obj.name)
            res.append(obj.level)
            res.append(obj.school_nid)
            res2.append(res)
            res = []
        if [name,level,school_nid] in res2:
            raise Exception('\033[43;1m[%s] [%s]教师 已经存在,不可重复创建\033[0m' % (name, level))


        s1 = modules.Teacher(name,level,school_nid)
        s1.save()
        status = True
        error = ''
        data = ('\033[33;1m 创建成功\033[0m' )
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}


def show_teacher():
    for obj  in  modules.Teacher.get_info_all():
        print("名字",obj.name,"等级",obj.level,"学校",obj.school_nid)


def create_course():
    try:
        print(modules.School.get_info_all())
        school_list = modules.School.get_info_all()
        # print("cccccccccccc",school_list)
        for k,obj in enumerate(school_list):
            print(k,obj.name,obj.addr)
        school = int(input("学校是（编号）："))
        school_obj = school_list[school]
        name = input("课程名字：")
        period = input("课程周期：")
        price = input("价格是")
        res2 = []
        for obj  in  modules.Course.get_info_all():

            res = []
            res.append(obj.name)
            res.append(obj.school_nid.uuid)
            res2.append(res)
            res = []

        print("ccccc",res2)
        print([name,school_obj.nid.uuid])
        print(type(res2))
        if [name,school_obj.nid.uuid] in res2:
            print("uuu")
            raise Exception('\033[43;1m[%s] 课程 已经存在,不可重复创建\033[0m' % (name))
        res2 =[]
        # school_nid = modules.School.get_info_all()
        s1 = modules.Course(name,period,price,school_obj.nid)
        s1.save()
        status = True
        error = ''
        data = ('\033[33;1m 创建成功\033[0m' )
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}
def show_course():
    for obj in modules.Course.get_info_all():
        print("学校[%s] 地点[%s] 课程名[%s] 价格[%s] 周期[%s]"\
        % (obj.school_nid.get_obj_by_uuid().name, obj.school_nid.get_obj_by_uuid().addr , obj.name,\
            obj.period,obj.price))

def create_course_to_teacher():
    try:
        print(modules.School.get_info_all())
        school_list = modules.School.get_info_all()
        # print("cccccccccccc", school_list)
        for k, obj in enumerate(school_list):
            print(k, obj.name, obj.addr)
        school = int(input("学校是（编号）："))
        school_obj = school_list[school]
        show_teacher()
        teacher_name = input("老师的名字")
        show_course()
        course_name =  input("课程名")
        res2 = []
        print(modules.Course_to_Teacher.get_info_all())
        for obj2 in  modules.Course_to_Teacher.get_info_all():
            res = []
            res.append(obj2.teacher_name)
            res.append(obj2.course_name)
            res.append(obj2.school_nid)
            res2.append(res)
            res = []
        if [teacher_name,course_name,school_obj.nid] in res2:
            raise Exception('\033[43;1m[%s] [%s] 已绑定  已经存在,不可重复创建\033[0m' % (course_name,teacher_name))
        s1 = modules.Course_to_Teacher(teacher_name,course_name,school_obj.nid)
        s1.save()
        status =True
        error =""
        res2= []
        data = ('\033[33;1m 创建成功\033[0m  老师：%s  课程：%s' %(teacher_name,course_name) )
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}


def show_create_course_to_teacher():
    obj = modules.Course_to_Teacher.get_course_to_teacher_list()
    res2 = []
    for k,obj2  in enumerate(obj):
        res2.append(obj2)
        print(k,"老师：",obj2.teacher_name,'课程:',obj2.course_name,"学校：",obj2.school_nid)
    return res2
    # modules.School.get_info_all()

def create_classes():
    try:
        obj3 = ''
        school_list = modules.School.get_info_all()  #是个列表
        res = []
        res2 = []
        for k,obj  in enumerate(school_list):
            print(k,obj.name,obj.addr)
            res.append(k)
            res2.append(obj.name)
            res2.append(obj.addr)
        school_n = int(input("学校是(输入编号)："))
        school_obj = school_list[school_n]
        #判断是否在k中
        classe_n = input("你的班级名字是：")
        # name, tuition, teacher, school_nid
        classe_tuition = input("班级的学费是：")

        res3 = show_create_course_to_teacher()
        # print(res3)
        c_to_t = int(input("你想关联那个(请输入编号):"))
        # res[c_to_t]
        # for obj in
        # if [classe_n,classe_tuition,res2[c_to_t]] in
        s1 = modules.Classes(classe_n,classe_tuition,(res3[c_to_t].teacher_name,res3[c_to_t].course_name),school_obj.nid)
        # print("cccccccccccc",show_classes())
        print([s1.name,school_obj.name])
        if [s1.name,school_obj.name]  in show_classes()['l']:
        # if [s1.name, school_obj.name] in show_classes(school_obj.name)['l']:

            raise Exception('\033[43;1m[%s] 课程  已经存在,不可重复创建\033[0m' % s1.name)
        status = True
        error = ""
        res2 = []
        s1.save()
        data = ('\033[33;1m 创建成功\033[0m')
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}



    # school_nid =





def show_classes():
    classes_l = modules.Classes.get_info_all()

    res1 =[]
    # res2 = []
    for obj  in classes_l:
        # if obj.school_nid.get_obj_by_uuid().name =:
        res1.append([obj.name,obj.school_nid.get_obj_by_uuid().name])
        print("班级名称",obj.name,"班级学费",obj.tuition,"学校",obj.school_nid.get_obj_by_uuid().name ,"学校地址",
              obj.school_nid.get_obj_by_uuid().addr,"关联状态[老师名字-课程名]",obj. course_to_school)###course_to_school
    return  {'status': '', 'error': '', 'data': '',"l":res1}
    # tuition,teacher,school_nid



def create_student():
    try:
        student_name = input("学生的名字：")
        student_age = input("学生的年龄：")
        student_qq = input("学生的qq号：")
        school_list = modules.School.get_info_all()  # print("cccccccccccc", school_list)
        for k, obj in enumerate(school_list):
            print(k, obj.name, obj.addr)
        school_name =int(input("学校名称(请输入编号)："))
        school_obj = school_list[school_name]
        dic3 = {'school_name':school_obj.name}
        show_classes()

        class_list = modules.Classes.get_info_all()
        for k, obj in enumerate(class_list):
            print(k, obj.name)
        class_name = int(input("班级名称(请输入编号)："))
        class_obj = class_list[class_name]
        res2 = []
        for obj  in  modules.Student.get_info_all():
            res = []
            res.append(obj.name)
            res.append(obj.age)
            res2.append(res)
            res = []
        if [student_name,student_age] in res2:
            print("uuu")
            raise Exception('\033[43;1m[%s] 学生 已经存在,不可重复创建\033[0m' % (student_name))
        s1 = modules.Student(student_name,student_age,student_qq,school_obj.nid,class_obj.nid)
        s1.save()
        # if [name,school_obj.nid.uuid] in res2:
        #     print("uuu")
        res2 =[]
        # school_nid = modules.School.get_info_all()
    #     s1 = modules.Course(name,period,price,school_obj.nid)
    #     s1.save()
        status = True
        error = ''
        data = ('\033[33;1m 创建成功\033[0m' )
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data,"name":student_name,"age":student_age,"tuition":'',"class_name":class_obj,'tuition_status':'Flase'}


def show_student():
    student_list = modules.Student.get_info_all()
    for obj in student_list:
        print("aaaaa",obj,type(obj))
        print("学生的名字",obj.name,"学校的名字", obj.school_nid.get_obj_by_uuid().name,"班级的名字",obj.classes_nid.get_obj_by_uuid().name)

def dic():
    dic2 ={
        '0': show_choice,
        '1': create_school,
        '2': show_school,
        '3': create_teacher,
        '4': show_teacher,
        '5': create_course,
        '6': show_course,
        '7': create_course_to_teacher,
        '8':  create_classes,
        '9': show_classes,
        '10': create_student,
        '11': show_student,
        '12': exit
    }
    return dic2


def login():
    show_choice()
    while True:
        choice = input("你想做什么:(请输入编号)")
        if choice not in dic().keys():
            print("请重新输入")
            continue
        ret = dic()[choice]()  # ret = 函数运行的结果

        if ret:
            if ret.get('status') :
                print(ret.get('data'))
            else:
                print(ret.get('error'))










