#
# @lc app=leetcode.cn id=2319 lang=python
#
# [2319] 判断矩阵是否是一个X矩阵
#
# 解法1(T92% S47%)：没啥好说的，总归是要把所有元素遍历一遍的，这题主要是考对角线上元素的下标

# @lc code=start
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i==j or i+j==len(grid)-1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True
# @lc code=end