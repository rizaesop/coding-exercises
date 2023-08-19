#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        p = self.removeElement(nums,0)
        for i in range(p,len(nums)):
            nums[i]=0
        return nums
    def removeElement(self,nums,val):
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow +=1
            fast +=1
        return slow

                
# @lc code=end

# 先删除所有的0，再加上所有的0