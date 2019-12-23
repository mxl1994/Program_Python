#!/usr/bin/python
# -*- coding: UTF-8 -*-

from  threading import Thread
import time

def task():
    num = 0
    while True:
        if num<=10:
            print('我是一只小财年')
            time.sleep(1)
            num+=1
        else:
            break
def download(n):
    images = ["girl,jpg", "boy.jpg", "man.jpg"]
    for im in images:
        print "正在下载", im
        time.sleep(n)
        print('下载{}成功！'.format(im))

def listenMusic(n):
    musics = ["高飞", "竹", "小苹果"]
    for music in musics:
        # print "正在下载", music
        time.sleep(n)
        print('正在听{}音乐'.format(music))

if __name__ == '__main__':
    th = Thread(target=download,name='aa',args=(1,))
    th.start()
    th1 = Thread(target=listenMusic, name='bb', args=(1,))
    th1.start()
    th.join()
    th1.join()


    print('*****over*****')