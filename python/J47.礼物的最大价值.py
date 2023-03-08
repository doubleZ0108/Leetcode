#
# @lc app=leetcode.cn id=J47 lang=python
#
# [剑指Offer 47] 礼物的最大价值
#
# 解法1(T89% S34%)：非常经典的动态规划问题，跟Leetcode62不同路径题基本一致，dp[i][j]代表走到(i, j)时能拿到礼物的最大价值，要么是从上面拿，要么是从左边拿，因此只要选择二者中最大的值拿即可，可以直接在原数组上dp

# @lc code=start
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]
# @lc code=end