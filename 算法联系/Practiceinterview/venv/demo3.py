# -*- coding:utf-8 -*-

def sort(nums):
    length = len(nums)
    for i in range(length):
        for j in range(length-i):
            if nums[j] > nums[j+1]:
                temp = nums[j+1]
                nums[j+1] =nums[j]
                nums[j] = temp
    return  nums


