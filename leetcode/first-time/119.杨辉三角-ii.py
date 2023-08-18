#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        curRow = []
        curRow.append(1)
        if rowIndex == 0:
            return curRow
       
        preRow = self.getRow(rowIndex - 1)
        for i in range(len(preRow)-1):
            curRow.append(preRow[i] + preRow[i+1])
        curRow.append(1)
        return curRow
# @lc code=end

