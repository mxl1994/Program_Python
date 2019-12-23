#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading

money = 1000

def run1():
    global money
    for i in range(100):
        money -= 1

def run2():
    global money
    for i in range(100):
        money -= 1

if __name__ == '__main__':
    th1 = threading.Thread(target=run1)
    th2 = threading.Thread(target=run2)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print money