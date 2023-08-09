#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

# @lc code=end

# 2023-08-09
# 只判断当前与后一个是否匹配；测试用例过了，提交用例挂了，摆烂果然是没有好结果的；；