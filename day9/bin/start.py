__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import configparser
import sys,os
import paramiko
BASE_PATH =  os.path.dirname(os.path.dirname( os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from common import parse,ssh_connect,ssh_up_get,show_conf
from src import src
# dict1 = {
#     "batch_run": ssh_connect.ssh_con,
#     "batch_scp": ssh_up_get.ssh_ftp,
#
#
# }



if __name__ == '__main__':
    while True:
        show_conf.show_conf()
        cmd = input("cmd:>>>").strip()
        # for i  in  dict1.keys():
        #     if cmd_l[0] not in i:
        #         print("命令错误，请重新输入")
        #         break
        # parse.parse(cmd_l)

        src.handle(cmd)