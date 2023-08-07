#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return (i,j)
# @lc code=end

# update: 2023-08-05
# 1. 语法不熟练
# 2. len()函数的作用，等于nums.size()，数组元素数量
# 3. 这个结构，可以不用判断 i != j ，但是复杂度还是很大。