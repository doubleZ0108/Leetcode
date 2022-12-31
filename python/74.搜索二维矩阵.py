#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#
# 解法1(T96% S65%): 没什么技巧，直接双重遍历，如果找到了就返回True，如果遇到一个比target大的后面都不用看了，直接返回False

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target: return True
                elif matrix[i][j] > target: return False
        return False
# @lc code=end

