#
# @lc app=leetcode.cn id=2373 lang=python
#
# [2373] 矩阵中的局部最大值
#
# 解法1(T42% S5%)：二维数组的遍历，结果维度肯定是(n-1)x(n-1)，因此i和j也都从1开始循环到n-1结束，再通过一个二重循环遍历周围的9个数并找到最大值，最终放在结果小数组的i-1 j-1位就刚好

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0]*(n-2) for _ in range(n-2)]
        for i in range(1, n-1):
            for j in range(1, n-1):
                tmp = 0
                for a in range(i-1, i+2):
                    for b in range(j-1, j+2):
                        tmp = max(tmp, grid[a][b])
                res[i-1][j-1] = tmp
        return res
# @lc code=end