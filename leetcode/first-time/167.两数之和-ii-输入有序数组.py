#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers)-1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1,j+1]
            elif sum <target :
                i += 1
            elif sum > target:
                j -= 1
        return [-1,-1]
                
            

# @lc code=end

