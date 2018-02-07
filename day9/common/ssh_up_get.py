__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import paramiko
def ssh_ftp_put(ip,port,user,passwd,local,remote):
    transport = paramiko.Transport((ip, port))
    transport.connect(username=user, password=passwd)

    sftp = paramiko.SFTPClient.from_transport(transport)
    # 将location.py 上传至服务器 /tmp/test.py
    sftp.put(local, remote)
    # 将remove_path 下载到本地 local_path
    # sftp.get('remove_path', 'local_path')

    transport.close()

def ssh_ftp_get(ip,port,user,passwd,remote,local):
    transport = paramiko.Transport((ip, port))
    transport.connect(username=user, password=passwd)

    sftp = paramiko.SFTPClient.from_transport(transport)
    # 将location.py 上传至服务器 /tmp/test.py
    # sftp.put('/tmp/id_rsa', '/etc/test.rsa')
    # 将remove_path 下载到本地 local_path
    sftp.get(remote, local)

    transport.close()