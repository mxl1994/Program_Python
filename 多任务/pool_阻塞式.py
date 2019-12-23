#!/usr/bin/python
# -*- coding: UTF-8 -*-

from multiprocessing import Pool
import os
from random import random
import time

def task1(task_name):
    print(("starting do {},id:{}").format(task_name,os.getpid()))
    start = time.time()

    time.sleep(random()*2)

    end = time.time()

    print "完成任务{}用时：{},进程id:{}".format(task_name,(end-start),os.getpid())
    # return "完成任务{}用时：{},进程id:{}".format(task_name,(end-start),os.getpid())

container = []

def func(n):

    container.append(n)
    # print(container)

if __name__ == '__main__':

    # print (random()*3)

    pool = Pool(5)

    tasks = ["听音乐","看电视剧","吃饭","睡觉","写作业","散步","打游戏","看孩子","做饭","洗衣服"]

    for task in tasks:
        try:
            pool.apply(task1, args=(task,))
        except:
            print("errot")
        # p.apply_async(task1, args=(task,))

    pool.close()
    pool.join()
    # print(container)
    for c in container:
        print(c)

    print("*************end*************")