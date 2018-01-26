__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import pickle
from conf import setting
from lib import commom
from src import iden
import os
class base:
    def save(self):
        #存,将对象序列化.
        print("cccccccccccccccc",type(self.nid),self.nid)
        print(self.path_db)
        path = os.path.join(self.path_db,str(self.nid))
        pickle.dump(self,open(path,'wb'))


    @classmethod      #不要绑定，否则只能用对象去触发。
    def get_info_all(cls):
        ret = []
        for file_name in  os.listdir(cls.path_db):
            file_path = os.path.join(cls.path_db,file_name)
            ret.append(pickle.load(open(file_path,'rb')))
        return ret

    @classmethod
    def get_course_to_teacher_list(cls):
        res =[]
        for file_name in os.listdir(cls.path_db):
            res.append(pickle.load(open((os.path.join(cls.path_db, file_name)),'rb')))
        return res


class School(base):
    #写入文件
    path_db = setting.SCHOOL_PATH
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.nid = iden.School_nid(self.path_db)



        
    # def save(self):
    #     #存,将对象序列化，
    #     pickle.dump(self,open( 'wb'))
    #读取信息


class Teacher(base):
    path_db = setting.TEACHER_PATH
    def __init__(self, name, level,school_nid):
        self.name = name
        self.level = level
        self.school_nid = school_nid
        self.nid = iden.Teacher_nid(self.path_db)

    # 关联学校


class Course_to_Teacher(base):
    path_db = setting.COURSE_TO_TEACHER
    def __init__(self,teacher_name,course_name,school_nid):
        self.teacher_name =teacher_name
        self.course_name = course_name
        self.school_nid = school_nid
        self.nid  = iden.Course_to_Teacher(self.path_db)

    # def get_course_to_teacher_list(self):
    #     for file_name  in os.listdir(self.path_db):
    #         return pickle.load(open(os.path.join(self.path_db,file_name)))


class Course(base):
    path_db = setting.COURSE_PATH
    def __init__(self, name,price,period,school_nid):  #school_obj.nid
        self.name = name
        self.price = price
        self.period = period
        self.school_nid = school_nid
        self.nid = iden.Course_nid(self.path_db)



class Student(base):
    path_db = setting.STUDENT_PATH
    def __init__(self,name,age,qq,school_nid,classes_nid):
        self.name =name
        self.age = age
        self.qq =qq
        self.school_nid =school_nid
        self.classes_nid =classes_nid
        self.nid = iden.Student_nid(self.path_db)



# 选择学校，关联班级

class Classes(base):
    path_db = setting.CLASSES_PATH
    def __init__(self,name,tuition,course_to_teacher,school_nid):
        self.name =name
        self.tuition = tuition
        self.school_nid  =school_nid
        self.course_to_teacher = course_to_teacher
        self.nid = iden.Classes_nid(self.path_db)

    # 关联课程
    # 关联讲师

class Grade(base):
    path_db = setting.GRADE_PATH
    def __init__(self,student_name,classes_name,course_name,count):
        self.student_name = student_name
        self.course_name = course_name
        self.classes_name = classes_name
        self.count = count
        self.nid = iden.Grade_Nid(self.path_db)






