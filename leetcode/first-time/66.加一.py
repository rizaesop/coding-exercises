#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        i = len(digits)-1
        while i >= 0:
            if digits[i]!= 9:
                digits[i]=digits[i]+1
                return digits
            else: 
                digits[i]=0
                i -= 1
        return [1]+[0] * len(digits)                
# @lc code=end

# 这个return句真神奇啊···