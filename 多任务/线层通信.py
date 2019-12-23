#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
from multiprocessing import Queue,JoinableQueue
# import queue
import time
import random

def produce(q):
    i=0
    while i < 10:
        num = random.randint(1,100)
        q.put("%d" % num)
        print("生产者产生数据：%d" % num)
        time.sleep(1)
        i +=1
    q.put(None)
    q.task_done()


def consume(q):
    # i =10
    while True:

        item = q.get()
        if item is None:
            break
        print("消费者获取到：%s" % item)
        # i -=1
        time.sleep(4)
    q.task_done()

if __name__ == '__main__':

    q = JoinableQueue(10)

    th1 = threading.Thread(target=produce,args=(q,))
    th1.start()

    th2 = threading.Thread(target=consume,args=(q,))
    th2.start()

    th1.join()
    th2.join()

    print('over')