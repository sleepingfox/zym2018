__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import paramiko

def ssh_con(ip,port,user,passwd,cmd):
    print(ip)
    print(port)
    print("conconconconcon")
    transport = paramiko.Transport((ip, port))
    print("bbbbb")
    transport.connect(username=user, password=passwd)

    ssh = paramiko.SSHClient()
    ssh._transport = transport
    print("sssssssssssssss",cmd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    res=stdout.read()
    print(res.decode('utf-8'))

    transport.close()
    print("ggggggg")

# ip = '192.168.254.128'
# port = 22
# user =
# ssh_con()