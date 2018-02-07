__author__ = 'Administrator'
# -*- coding: utf-8 -*-

# from  socket import *
#
# server = socket(AF_INET,SOCK_DGRAM)
# server.bind(("127.0.0.1",8081))
#
# while True:
#     data,client_addr = server.recvfrom(1024)
#     print(data,client_addr)
#     server.sendto(data.upper(),client_addr)


# dic1 = {
#
# }
#
#
#
# dic1.setdefault(1,{})
# print(dic1)

from threading import Thread,Lock
import time

n=100
def task():
    print("testsetsetsetsetsetsetets")
    time.sleep(3)
if __name__ == '__main__':
    while True:
        input("cmd>>>>")
        start_time=time.time()
        t_l=[]
        for i in range(2):
            t=Thread(target=task)
            t_l.append(t)
            t.start()

        for t in t_l:
            t.join()
        stop_time=time.time()
        print('主',n)
        print('run time is %s' %(stop_time-start_time))



















