#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        # 初始情况
        if numRows == 1:
            triangle = []
            firstRow = [1]
            triangle.append(firstRow)
            return triangle
       
        # 递归语句
        triangle = self.generate(numRows-1)

        bottomRow = triangle[-1] # 上一层
        newRow = [1] #新建一层
        for i in range(len(bottomRow)-1):
            newRow.append(bottomRow[i] + bottomRow[i+1])
        newRow.append(1)

        # 将递归结果加入
        triangle.append(newRow)
        
        # 返回上一层
        return triangle

# @lc code=end

