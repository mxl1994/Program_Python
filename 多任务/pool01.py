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

    # print "完成任务{}用时：{},进程id:{}".format(task_name,(end-start),os.getpid())
    return "完成任务{}用时：{},进程id:{}".format(task_name,(end-start),os.getpid())

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
            pool.apply_async(task1, args=(task,), callback=func)
        except:
            print("errot")
        # p.apply_async(task1, args=(task,))

    pool.close()
    pool.join()
    # print(container)
    for c in container:
        print(c)

    print("*************end*************")





# from multiprocessing import Process, Pool
# import os
# import time
# import random
#
#
# # 子进程任务
# def download(f):
#     print('__进程池中的进程——pid=%d,ppid=%d' % (os.getpid(), os.getppid()))
#     for i in range(3):
#         print(f, '--文件--%d' % i)
#         time.sleep(random.randint(1, 9))
#         # time.sleep(1)
#     return {"result": 1, "info": '下载完成！'}
#
#
# # 主进程调用回调函数
# def alterUser(msg):
#     print("----callback func --pid=%d" % os.getpid())
#     print("get result:", msg["info"])
#
#
# if __name__ == "__main__":
#     p = Pool(3)
#     p.apply_async(func=download, args=(1111,), callback=alterUser)
#     p.apply_async(func=download, args=(2222,), callback=alterUser)
#     p.apply_async(func=download, args=(3333,), callback=alterUser)
#     # 当func执行完毕后，return的东西会给到回调函数callback
#     print("---start----")
#     p.close()  # 关闭进程池，关闭后，p不再接收新的请求。
#     p.join()
#     print("---end-----")