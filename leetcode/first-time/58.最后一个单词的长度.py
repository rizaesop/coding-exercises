#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        # ans = 0
        # for i in range(len(s)):
        #     if 'a'<= s[i] and s[i]<='z':
        #         ans += 1
        #     elif s[i]== ' ' and s[i+1]:
        #         ans = 0
        # return ans
        right = len(s)-1
        while right>= 0:
            if s[right]!= ' ':
                break
            right -= 1
        if right == 0:
            return 1
        left = right
        while left >= 0:
            if s[left]==' ': 
                if left == 0:
                    return right
                break
            left -= 1
        return right-left
        
# @lc code=end