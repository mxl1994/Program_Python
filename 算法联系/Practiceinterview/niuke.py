# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array)<=1:
            return array
        for i in range(0,len(array)):
            if array[i] % 2 == 0:
                for j in range(i+1,len(array)):
                    if array[j] % 2 == 0:
                        if j == len(array) - 1:
                            return array
                        continue
                    if array[j] % 2 == 1:
                        count = j - i
                        temp = array[i]
                        array[i] = array[j]
                        # print array[i]
                        while count > 1:
                            array[i+count] = array[i+count-1]
                            count-=1
                        array[i+1]=temp
                    break
            else:
                continue
            print array


p = Solution()
a = [8,5,7,3,9,0,2,1,7]
p.reOrderArray(a)

print a
