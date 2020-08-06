# -*- coding:utf-8 -*-

from multiprocessing import   Pool

TREAD

def task(params):
    print params


if __name__ == "__main__":
    p = Pool(10)
    task1 = ["听音乐","上课",]
    for task in task1:

        p.apply_async(target = task,args=(task,))

    p.join()
    p.close()


大文件 一列 全是数字

name score__name



    select name,count(name)
    from tabke
    group by name
    having count(name)>10
    order by count(name)
    limit 10
create index indexname on tabke(字段)