#!/usr/bin/python
# -*- coding: UTF-8 -*-


from multiprocessing import Queue
from multiprocessing import Process
from time import sleep

#下载文件
def download(q):

    images = ["girl,jpg", "boy.jpg", "man.jpg"]
    for im in images:
        print "正在下载",im
        sleep(0.5)
        q.put(im,timeout=3)
    # print("download success..")

def savefile(q):
    while True:
        try:
            file = q.get(timeout=3)
            print "{} 保存成功".format(file)
        except:
            print ('全部保存成功')
            break

    # print("save success..")

if __name__ == '__main__':

    q = Queue(5)
    p1 = Process(target=download,args=(q,))

    p2 = Process(target=savefile,args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("********end********")