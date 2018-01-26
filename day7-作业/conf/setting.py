__author__ = 'Administrator'
# -*- coding: utf-8 -*-


import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHOOL_PATH = os.path.join(BASE_PATH,'db','school')
TEACHER_PATH = os.path.join(BASE_PATH,'db','teacher')
STUDENT_PATH = os.path.join(BASE_PATH,'db','student')
COURSE_PATH = os.path.join(BASE_PATH,'db','course')
CLASSES_PATH = os.path.join(BASE_PATH,'db','classes')
PID_PATH = os.path.join(BASE_PATH,'db','pid')
COURSE_TO_TEACHER = os.path.join(BASE_PATH,'db','course_to_teacher')
GRADE_PATH = os.path.join(BASE_PATH,'db','grade')