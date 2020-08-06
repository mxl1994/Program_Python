# -*- coding:utf-8 -*-
# class Solution:
#     def StrToInt(self, s):
#         # write code here
#         if s == "":
#             return 0
#         flag = 1 # 标明正负的符号
#         wei = 0  # 位数指针
#         num = 0  # 结果
#         if s[0] in "+-":
#             if s[0] == "+":
#                 flag = flag
#             else:
#                 flag *= -1  # 如果是-，就将flag变成-1
#             s = s[1:]   # 将第一个符号，去除
#         for i in range(len(s)-1,-1,-1):   # 从后往前遍历字符串
#             if s[i] not in "0123456789":    # 先检查是否合法
#                 return 0
#             else:                    # 结果加上当前字符*位数
#             # 字符“0”对应的ASCII码为48。对获得的字符串中的每个字符，
#             # 求其ASCII码，减去48即为对应位上的数值。
#                 num += (ord(s[i]) - 48)*(10**wei)
#                 wei += 1   # 位数每遍历一个字符，就要进一位
#         return num * flag       # 注意正负号
#
# p = Solution()
# result = p.StrToInt('-2147483649')
# print result
#
#
# def StrToInt(self, s):
#     # write code here
#     if not s:
#         return 0
#     str2num={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
#     flag2num={'-':-1,'+':1}
#     first=s[0]
#     if first in ['+','-']:
#         flag=flag2num[first]
#         if len(s) == 1:
#             return 0
#         x=0
#         for i in s[1:]:
#             if i not in str2num:
#                 return 0
#             x=x*10+str2num[i]
#         return flag*x
#     else:
#         x=0
#         for i in s:
#             if i not in str2num:
#                 return 0
#             x=x*10+str2num[i]
#         return x
#
#
# # -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def deleteDuplication(self, pHead):
#         # write code here
#         if not pHead or pHead.next == None:
#             return pHead
#         head = ListNode(None)
#         head.next = pHead
#         pre = pHead
#         cur =pHead.next
#         while cur != None:
#             if cur.next!=None and cur.val==cur.next.val:
#                 while cur.next!=None and cur.val==cur.next.val:
#                     cur = cur.next
#                 cur = cur.next
#                 pre.next = cur
#             else:
#                 pre = cur
#                 cur = cur.next
#         return head.next


# -*- coding:utf-8 -*-
 #class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
# class Solution:
#     def Print(self, pRoot):
#         # write code here
#         if not pRoot:
#             return None
#         queue = []
#         res = []
#         temp = []
#         level=0
#         toBePrinted = 1
#         isEven = True
#         queue.append(pRoot)
#         while queue:
#             node = queue.pop(0)
#             if node.left:
#                 queue.append(node.left)
#                 level +=1
#             if node.right:
#                 queue.append(node.right)
#                 level+=1
#             toBePrinted-=1
#             if toBePrinted==0:
#                 if isEven:
#                     res.extend(temp)
#                 else:
#                     res.extend(temp.reverse())
#                 temp = []
#                 toBePrinted = level
#                 level = 0
#                 isEven = bool(1-isEven)
#         return res
# p = Solution()
# result = p.Print()
# print result


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix  or  not path :
            return False
        visited = [0] * len(matrix)
        result = ''
        length = 0
        for row in range(rows):
            for col in range(cols):
                if (self.hasPathCore(matrix, path, rows, cols, row, col, visited, result, length)):
                    return True
        del visited
        return False

    def hasPathCore(self, matrix, path, rows, cols, row, col, visited, result, length):
        if result == path:
            return True
        hasPath = False
        if (row >= 0 and row < rows and col >= 0 and col < cols and (not visited[row*cols + col])\
            and path[length] == matrix[row*cols + col]):
            length += 1
            visited[row*cols + col] = 1
            result += matrix[row*cols + col]
            hasPath = self.hasPathCore(matrix, path, rows, cols, row-1, col, visited, result, length) or \
                      self.hasPathCore(matrix, path, rows, cols, row+1, col, visited, result, length) or \
                      self.hasPathCore(matrix, path, rows, cols, row, col+1, visited, result, length) or \
                      self.hasPathCore(matrix, path, rows, cols, row, col-1, visited, result, length)
            if (not hasPath):
                length -= 1
                visited[row*cols + col] = 0
                result = result[:-1]
        return hasPath

p = Solution()
re = p.Deserialize('2!#!4!2!7!')
print re
