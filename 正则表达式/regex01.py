#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# mas = "佟丽娅娜扎热巴代斯"
#
# re.compile(mas)


# s= '娜扎热巴代斯佟丽娅'
# result = re.search('佟丽娅',s)
# print result.span()
# print result.group()

# #search() 只要找到一个不会继续向下找
# msg = 'jskaj8dsjf23njsjfd2jkdjj'
# result = re.search('[a-z][0-9][a-z]',msg)
# # print result.span()
# print result.group()
#
# #findall()匹配整个字符，找到一个继续向下找一直到字符串结尾
# result = re.findall('[a-z][0-9][a-z]',msg)
# print result


#a7a a88a a7878a

# msg = 'a7aopa88asjdfja7878a'
# result = re.findall('[a-z][0-9]+[a-z]',msg)
# print result

#验证输入的邮箱
# msg = "1329541259@qq.com"
# result = re.match('[1-9][\d]{9}@(qq|163)\.(com|cn)$',msg)
# # result = re.match('\w{5,20}@(qq|163)\.(com|cn)$',msg)
# print result
# # print result.group()
# # print result.group(1)
# # print result.group(2)
# # print result.start(2)
# # print result.end(2)
# print result.endpos

#不是以4、7结尾的手机号码（11位 ）
# msg = '171560892682'
# result = re.match('1\d{9}[0-35-689]',msg)
# print result


#分别提取
#区号
# phone = '010-12345678'
# result = re.match(r'(\d{3}|\d{4})-(\d{8})$',phone)
# print result
# print result.group(1)
# print result.group(2)


#标签网页
#引用分组的方式（2种）

msg = '<html>abc</html>'
msg1 = '<h1>hi</h1>'

# result = re.match('<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$',msg)



#number
# result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$',msg1)
# print result
# # print result.group(1)


#(?P<name>)
result = re.match(r'<(?P<name1>[0-9a-zA-Z]+)>(.+)</((?P=name1))>$',msg)
print result
print result.groups()
print result.group(1)
print result.group(2)
print result.group(3)