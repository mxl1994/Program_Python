# -*- coding:utf-8 -*-

def merge(l1,l2):
    len1 = len(l1)
    len2 = len(l2)
    right1 = len1-1
    right2 = len2-1
    index = len1+len2-1
    while l1 and l2:
        if l1[right1] >= l2[right2]:
            l1[len1+len2-1] = len1[right1]
            right1 = right1-1

        else:
            l1[len1 + len2 - 1] = len1[right2]
            right2 = right2-1
        len
    if l2:
        for i in l2[]



































def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return -1
    l = len(s)
    dic = {}
    for i in range(l):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1
    print dic
    for j in range(l):
        if dic[s[j]] == 1:
            return j
    return -1

firstUniqChar("loveleetcode")

