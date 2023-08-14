#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val): 
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast]!=val :
                nums[slow]=nums[fast]
                slow +=1
            fast += 1
        return slow
        
# @lc code=end

