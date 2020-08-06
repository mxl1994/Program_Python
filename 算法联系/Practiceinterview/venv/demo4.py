# -*- coding:utf-8 -*-

from threading import Thread

t1 = Thread(target=test)
lists = [a,b,c,d]
t1.start()
# t1.xx(aa=test,)
t1.jion()

def test():
    for i in lists:
        print i