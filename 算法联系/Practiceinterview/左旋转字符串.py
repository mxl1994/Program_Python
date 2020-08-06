# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        lenght = len(s)
        if lenght == n:
            return s
        m = n%lenght
        lstr = list(s)
        newlstr = lstr[:m]
        print newlstr
        newrstr = lstr[m:]
        print newrstr
        newrstr.extend(newlstr)
        result = ''.join(newrstr)
        return result

p = Solution()
result = p.LeftRotateString('cdefgab',2)
print result