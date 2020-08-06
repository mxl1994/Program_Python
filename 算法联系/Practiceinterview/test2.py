# encoding:utf-8
list = [1,2,3,4,5]
def fn(x):
    return x**2
result = map(fn,list)
result = [i for i in result if i > 10]
print result

a = 3
assert(a > 1)
print("111")

s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort(reverse=False)
res = "".join(s)
print(res)


dict={"name":"zs","age":18,"city":"shenzhen","tel":"1362626627"}
list = sorted(dict.items(),key=lambda i:i[0],reverse=False)
print (list)
new_dict ={}
for i in list:
    new_dict[i[0]] = i[1]
print(new_dict)

from collections import Counter
str = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(str)
print(res)

import re
a = "not 404 found 张三 99 深圳"
list = a.split(" ")
print(list)
res = re.findall('\d+|[a-zA-Z]+',a)
for i in res:
    if i in list:
        list.remove(i)
new_str = " ".join(list)
print(res)
print(new_str)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fn(a):
    return a%2==1
newlst = filter(fn,a)
print(newlst)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = [i for i in a if i%2==1]
print(newlist)

list1 = [1,5,7,9]
list2 = [2,2,6,8]
list1.extend(list2)
print(list1)
list1.sort(reverse=False)
print(list1)

import datetime
print(datetime.datetime.now())

def fn():
    try:
        for i in range(5):
            if i>2:
                raise Exception("数字大于2了")
    except Exception as ret:
        print(ret)
fn()

a = [[1,2],[3,4],[5,6]]
print([j for i in a for j in i])

x="abc"
y="def"
z=["d","e","f"]
m = x.join(y)
print(m)
n = x.join(z)
print(n)

try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了:%s'%errorMsg)
else:
    print('没有捕获到异常，则执行该语句')

try:
    num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了:%s'%errorMsg)
finally:
    print('不管是否捕获到异常，都执行该语句')

a,b = 3,4
print(a,b)
a,b = b,a
print(a,b)

import re
a="张明 98分"
new_a = re.sub(r"\d+","100",a)
print(new_a)

a = b"hello"
b = "哈哈".encode()
print(a,b)
print(type(a),type(b))