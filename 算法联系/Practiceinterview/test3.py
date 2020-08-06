# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     # 返回镜像树的根节点
#     def Mirror(self, root):
#         # write code here
#         if root == None:
#             return None
#         if root.left == None and root.right == None:
#             return None
#         temp = root.right
#         root.right = root.left
#         root.left = temp
#         if root.left:
#             self.Mirror(root.left)
#         if root.right:
#             self.Mirror(root.right)
#
#
# # -*- coding:utf-8 -*-
# class Solution:
#     def IsPopOrder(self, pushV, popV):
#         # write code here
#         if len(pushV)!=len(popV):
#             return False
#         stack = []
#         j=0
#         for i in range(len(pushV)):
#             stack.append(pushV[i])
#             while j<len(popV) and stack[len(stack)-1]==popV[j]:
#                 stack.pop()
#                 j+=1
#         if stack:
#             return False
#         else:
#             return True





# # -*- coding:utf-8 -*-
# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#         # write code here
#         numbers=list(numbers)
#         dicts={}
#         new_list=[]
#         for i in numbers:
#             if i not in dicts.keys():
#                 dicts[i]=0
#                 dicts[i]+=1
#             else:
#                 dicts[i]+=1
#         for k,v in dicts.items():
#             if v > len(numbers)//2:
#                 new_list.append(k)
#             else:
#                 continue
#         if len(new_list)==0:
#             return 0
#         for i in new_list:
#             return i
# s = Solution()
# result = s.MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3])
# print result


# # -*- coding:utf-8 -*-
# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
#         # write code here
#         if len(tinput) <= k:
#             print len(tinput)
#             return tinput.sort()
#         else:
#             print 111
#             tinput.sort(reverse=True)
#             print len(tinput)
#             new_list = tinput[len(tinput)-1:len(tinput)-(k+1):(-1)]
#             print len(tinput)
#             print new_list
#             return new_list
# p=Solution()
# p.GetLeastNumbers_Solution([1,2,3,4,5,6,7,8,9],8)
# # print  result
