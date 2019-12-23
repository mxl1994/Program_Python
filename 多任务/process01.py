#!/usr/bin/python
# -*- coding: UTF-8 -*-

from multiprocessing import Process
import os
from time import sleep

def task1(n):
    while True:
        sleep(n)
        print("I am process1",os.getpid(), "*********")

def task2(n):
    while True:
        sleep(n)
        print("I am process2",os.getpid(), "*********")

if __name__ == '__main__':
    print(os.getpid())

    p1 = Process(target=task1, name="子进程1",args=(1,))
    p1.start()

    p2 = Process(target=task2, name="子进程2", args=(2,))
    p2.start()

    #p1.close()#进程没有close()方法
    p1.join()
    print("***************************")