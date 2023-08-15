#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        left = 0
        right = 0
        while right <= len(haystack):
            while len(haystack[left:right+1]) == len(needle):
                if haystack[left:right+1] == needle:
                    return left
                else:
                    left += 1
                    right += 1
            right += 1
        return -1
# @lc code=end

