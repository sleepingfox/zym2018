__author__ = 'Administrator'
# -*- coding: utf-8 -*-

# from  socket import *
#
# client = socket(AF_INET,SOCK_DGRAM)
#
# while True:
#     msg = input(">>>:").strip()
#     client.sendto(msg.encode('utf-8'),("127.0.0.1",8081))
#     data,server_addr = client.recvfrom(1024)
#
#     print(data.decode('utf-8'))


#
# from  multiprocessing import Process
# import time
# def task(name):
#     print("%s is running" %name)
#     time.sleep(3)
#     print("%s is down" %name)
#
# if __name__ == '__main__':
#     p = Process(target=task,args=('zym'))
#     p.start()

#方式二：
from  multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,name): #定义自己的属性会把父类覆盖掉
        super(MyProcess,self).__init__()     #重用父类
        self.name =name

    def run(self):
        print("%s is running" % self.name)
        time.sleep(3)
        print("%s is down" % self.name)

if __name__ == '__main__':
    p =MyProcess('进程一')
    p.start() # 就是p.run() 因为是自己定义的进程，所以要自己写run函数