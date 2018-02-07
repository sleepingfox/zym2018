__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from threading import Thread
from  common import ssh_connect,ssh_up_get,parse,show_conf
import configparser
from etc import setting
import os
dict1 = {
    "batch_run": ssh_connect.ssh_con,



}


def handle(cmd):
    # while True:
    print(os.path.abspath(__file__))
    for i  in  dict1.keys():
        if cmd[0] not in i:
            print("命令错误，请重新输入")
            break

    #解析的结果，两个合并
    info  =  parse.parse(cmd)
    print(info)                 #[['h1'], ['web_clusters,db_servers'], ['"df -h"']]

    #进行2次 数据整理
    cmd_l = cmd.split()
    print("hhhhhhhhhhhhh")
    host = info[0][0]
    print(host)
    group = info[1][0]
    print(group)
    g_l = group.split(",")   #[web_clusters db_servers]
    h_l = host.split(",")      # [h1 h2]
    #######################

    #查找信息：
    config = configparser.ConfigParser()
    config.read(setting.CONF_PATH)
    conf_l = []
    for section in g_l:
        # conf_l[section] = {}
        count = 0
        for h in h_l:                     #这里有点需要注意：如果一个ip在不同的组里面会创建多个链接。

            temp = config.get(section,h)
            count+=1
            print("temp",temp,type(temp))
            conf_l.append(temp)
            print("conf_LLLLLLLLLLLLLL",conf_l)

    if cmd_l[0] == 'batch_run':
        cmd_cmd = info[2][0].strip('\"')
        print("cml_l",cmd)
        print("cmd_cmd",type(cmd_cmd),cmd_cmd)
        mmm = 0
        print("")
        for i in conf_l:
            temp = i.split()
            ip = temp[0]
            port = int(temp[3])
            user = temp[1]
            passwd = temp[2]
            t_l = []
            t = Thread(target=dict1[cmd_l[0]],args=(ip,port,user,passwd,cmd_cmd,))
            t_l.append(t)
            t.start()
        for i in t_l:
            i.join()
    print("成功")
                            # dict1[cmd_l[0]](ip,port,user,passwd,cmd_cmd)
    if cmd_l[0] == 'batch_scp':
        print(cmd)
        print(cmd_l)
        for i in conf_l:
            temp = i.split()
            ip = temp[0]
            port = int(temp[3])
            user = temp[1]
            passwd = temp[2]
            t_l=[]
            if cmd_l[6] =="put":
                print("putputputput")
                local = cmd_l[8]
                remote = cmd_l[10]
                t = Thread(target= ssh_up_get.ssh_ftp_put,args=(ip,port,user,passwd,local,remote,))
                # ssh_up_get.ssh_ftp_put(ip,port,user,passwd,local,remote)
                t_l.append(t)
                t.start()
            if cmd_l[6] =="get":
                print("getegetgetgetget")
                local = cmd_l[10]
                remote = cmd_l[8]
                t = Thread(target=ssh_up_get.ssh_ftp_get, args=(ip, port, user, passwd, remote, local,))
                # ssh_up_get.ssh_ftp_get(ip, port, user, passwd, local, remote)
                t_l.append(t)
                t.start()

        for i in t_l:
            i.join()
        print("成功")

