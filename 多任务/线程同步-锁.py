#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

list1 = [0]*10
lock = threading.Lock()
def task1():
    # lock.acquire()
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.1)
    # lock.release()


def task2():
    # lock.acquire()
    for i in range(len(list1)):
        print('---->',list1[i])
        time.sleep(0.1)
    # lock.release()


if __name__ == '__main__':

    th2 = threading.Thread(target=task2)
    th1 = threading.Thread(target=task1)

    th2.start()
    th1.start()

    th2.join()
    th1.join()

    print list1