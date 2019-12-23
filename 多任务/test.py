# mul = lambda x,y:x*y
# print mul(2,4)

# dict={"name":"2","age":18,"city":"4","tel":"1362626627"}
#
# for k in sorted(dict):
#     print k,dict[k]

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print [item for item in a if item % 2 != 0]



# a=(1,)
# b=(1)
# c=("1")
# print type(a)
# print type(b)
# print type(c)


list1 = [1,5,7,9]
list2 = [2,2,6,8]
list1.extend(list2)
print list1

print sorted(list1,reverse=True)

list1.sort(reverse=False)
print list1