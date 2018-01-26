__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from lib import commom
import os
import pickle
class Nid:
    def __init__(self,role,path_db):
        role_list = [
            'admin', 'school', 'teacher', 'course', 'Course_to_Teacher', 'classes', 'student',"grade"
        ]
        if role not in role_list:
            raise Exception('用户角色错误,选项: %s' % ','.join(role_list))
        self.role =role
        self.path_db = path_db
        self.uuid = commom.uuid_get()


    def __str__(self):
        return self.uuid

    # def get_obj_by_uuid(self):    #获取学校的对象,调用需要用点“。”
    #     for file_name in os.listdir(self.path_db):
    #         if file_name == self.uuid:
    #             return pickle.load(open(os.path.join(self.path_db,file_name)),'rb')
    #     return None
    def get_obj_by_uuid(self):
        for file_name in os.listdir(self.path_db):
            # print("ppppppppppp",self.path_db)
            if file_name == self.uuid:
               return  pickle.load(open(os.path.join(self.path_db,file_name),'rb'))




class School_nid(Nid):
    def __init__(self,path_db):
        super(School_nid,self).__init__('school',path_db)

class Teacher_nid(Nid):
    def __init__(self,path_db):
        super(Teacher_nid,self).__init__('teacher',path_db)

class Student_nid(Nid):
    def __init__(self,path_db):
        super(Student_nid,self).__init__('student',path_db)


class Course_nid(Nid):
    def __init__(self,path_db):
        super(Course_nid,self).__init__('course',path_db)

class Course_to_Teacher(Nid):
    def __init__(self,path_db):
        super(Course_to_Teacher,self).__init__('Course_to_Teacher',path_db)

class Classes_nid(Nid):
    def __init__(self,path_db):
        super(Classes_nid,self).__init__('classes',path_db)

class Grade_Nid(Nid):
    def __init__(self,db_path):
        super(Grade_Nid, self).__init__('grade',db_path)