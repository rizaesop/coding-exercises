#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        a = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        for i in range(len(s)):
            if i <len(s)-1 and a[s[i]] < a[s[i]]+1:
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans



# @lc code=end

# 这个是学讨论区一位大佬的写法。根本没想过可以用dict写；；他的写法简化了对字符串的
# 判断。