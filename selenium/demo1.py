#coding:utf-8


if __name__=='__main__':
    _list=[]
    for i in range(3):
        def func(a):
            return i+a
        _list.append(func)
    for f in _list:
        print(f(1))