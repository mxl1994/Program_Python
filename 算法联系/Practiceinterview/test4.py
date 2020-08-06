# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        pNode1 = 1
        p1 = pHead1
        while p1.next:
            pNode1 +=1
            p1 = p1.next
        pNode2 = 1
        p2 = pHead2
        while p2.next:
            pNode2 +=1
            p2 = p2.next
        if pNode1-pNode2 > 0:
            lens = abs(pNode1-pNode2)
            for i in range(lens):
                pHead1 = pHead1.next
            for j in range(pNode2):
                if pHead1 == pHead2:
                    return pHead1
        if pNode1-pNode2 < 0:
            lens = abs(pNode2-pNode1)
            for i in range(lens):
                pHead1 = pHead2.next
            for j in range(pNode1):
                if pHead1 == pHead2:
                    return pHead1