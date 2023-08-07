#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        # y 是 x 翻转后的数字
        y = 0
        while temp > 0:
            last_num = temp % 10
            temp = temp // 10
            # 从最高位生成数字的技巧
            y = y * 10 + last_num
        return y == x
# @lc code=end

# 一开始也想写一一对比的算法，但是没想到怎么写;;

