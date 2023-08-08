#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])): 
            for j in range(1,len(strs)):
                thisStr, preStr = strs[j], strs[j-1]
                if i >= len(thisStr) or i >= len(preStr) or thisStr[i] != preStr[i]:
                    return strs[j][:i]
        return strs[0]
# @lc code=end

