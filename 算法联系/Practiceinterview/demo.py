# -*- coding:utf-8 -*-
def findone(lis):
    n=len(lis)
    res = set()
    for i in range(n):
        if lis[i] in res:
            continue
        else:
            if lis.count(lis[i])==1:
                return lis[i]
            else:
                res.add(lis[i])
    return None


select * from table_student where cid=1 order by score desc limit 1 offset 1