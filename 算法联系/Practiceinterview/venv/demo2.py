# -*- coding:utf-8 -*-

def findquinnum(nums):
    length = len(nums)
    result = 0
    for i in range(length):
        result ^= nums[i]
        print result

nums = [2,3,4,2,3]
findquinnum(nums)