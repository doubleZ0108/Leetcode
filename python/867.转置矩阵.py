#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
# 解法1(T36% S67%)：感觉这道题更像是对二维数组和循环语法的理解，尤其是Python二维数组的语法本来应该是长宽两维反过来写，但转置矩阵本来长宽就反过来所以就顺这些mn就好了，直接两重循环原数组的ij位对应转置矩阵的ji位

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        T = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                T[j][i] = matrix[i][j]
        return T
# @lc code=end

