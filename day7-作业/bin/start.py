__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import sys
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(sys.path)
from src.service import admin_service
from src.service import teacher_service
from src.service import student_service


dic1 = {
    'admin':admin_service.login,
    'teacher':teacher_service.login,
    'student':student_service.login,

}


def  show_choice():
    msg = '''
    admin
    teacher
    student
    '''
    print(msg)
def run():
    while True:
        show_choice()
        role_user = input("你的角色：")
        user = ['admin','teacher','student']
        if role_user not in user:
            print("你输入的角色不存在请重新输入")
            continue
        dic1[role_user]()

if __name__ == '__main__':
    print(sys.path)
    run()


