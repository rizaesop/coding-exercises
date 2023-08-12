#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        fast = 1
        ans = len(nums)
        while (fast < ans):
            # 判断当前fast指针和slow指针
            if nums[slow] < nums[fast]:# fast 指针大于slow指针，所以移动slow指针
                slow+=1
                nums[slow]=nums[fast]
            fast +=1
        return slow + 1
# @lc code=end
# 2023-08-12 感觉可以用递归写，但还没想好。总之用了快慢指针，但出现问题。结论是不需要“else”。
# 只需要nums[slow]=nums[fast]，即可以维护无重复。
