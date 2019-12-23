#!/usr/bin/python
# -*- coding: UTF-8 -*-

from threading import Thread,Lock
import time


lockA = Lock()
lockB =Lock()

class MyThread(Thread):
    def run(self):
        if lockA.acquire():
            print(self.name+'获取了A锁')
            time.sleep(0.1)
            if lockB.acquire():
                print(self.name + '又获取了B锁,原来还有A锁')
                time.sleep(0.1)
                lockB.release()
            lockA.release()

class MyThread1(Thread):
    def run(self):
        if lockB.acquire():
            print(self.name+'获取了B锁')
            time.sleep(0.1)
            if lockA.acquire():
                print(self.name + '又获取了A锁,原来还有B锁')
                time.sleep(0.1)
                lockA.release()
            lockB.release()

if __name__ == '__main__':

    th1 = MyThread()
    th2 = MyThread1()

    th1.start()
    th2.start()

    th1.join()
    th2.join()