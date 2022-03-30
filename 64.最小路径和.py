#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#
# 解法1(T83% S43%): 经典动态规划
# dp[i][j]：从(0,0)走到(i,j)的路径长
# 目标：dp[m][n]
# 转移方程：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
# 初始化：第0行和第0列就是(0,0)直着走到自己

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j-1]


        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]
# @lc code=end

