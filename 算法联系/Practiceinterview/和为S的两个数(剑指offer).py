# # -*- coding:utf-8 -*-
# # class Solution:
# #     def FindNumbersWithSum(self, array, tsum):
# #         # write code here
# #         if len(array)<=1:
# #             return None
# #         if len(array)==2 and sum(array)==tsum:
# #             return array
# #         result = []
# #         j=0
# #         for i in range(len(array)):
# #             temp = tsum-array[i]
# #             if temp in array:
# #                 j = array.index(temp)
# #                 if i==j:
# #                     continue
# #                 result.append([array[i],array[j]])
# #             else:
# #                 array = array[array[i+1]:array[j]]
# #                 i=0
# #         if len(result)==0:
# #             return false
# #         if len(result)==1:
# #             return result[0][0],result[0][1]
# #         min_mul = result[0][0]*result[0][1]
# #         index = 0
# #         for i in range(1,len(result)):
# #             mul = result[i][0]*result[i][1]
# #             if mul < min_mul:
# #                 min_mul = mul
# #                 index = i
# #         return result[i][0],result[i][1]


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        result = []
        if len(array)<=1:
            return result
        left = 0
        right = len(array)-1
        while left<right:
            if (array[left]+array[right])==tsum:
                result.append(array[left])
                result.append(array[right])
                break
            elif array[left]+array[right]>tsum:
                right-=1
            else:
                left+=1
        return result