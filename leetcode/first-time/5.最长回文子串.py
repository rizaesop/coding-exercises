#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(0, len(s)):
            # 以 s[i] 为中心的最长回文子串
            s1 = self.checkif(s, i, i)
            # 以 s[i] 和 s[i+1] 为中心的最长回文子串
            s2 = self.checkif(s, i, i + 1)
            # res = longest(res, s1, s2)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res
    
    def checkif(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]



# @lc code=end

# 2023-08-20 需要定义两个字符串，因为有可能是单个字符中心，或者是两个相同的字符中心
# 反正定义的函数内会check这两个相同的字符是否相等。
