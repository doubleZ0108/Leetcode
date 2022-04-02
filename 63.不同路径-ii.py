#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#
# 解法1(T82% S90%): 上一道题的约束变种，在传播过程中只要遇到有石头的就continue跳过即可，比较复杂的是初始化阶段，要从右下角向上和向左初始化两条边，如果遇到石头就break不初始化上面和左边一段，此外还要判断左上角和右下角是不是有石头

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] or obstacleGrid[m-1][n-1]:
            return 0

        dp = [[0]*n for _ in range(m)]
        for i in range(m-1, -1, -1):
            if obstacleGrid[i][n-1]:
                break
            dp[i][n-1] = 1
        for j in range(n-1, -1, -1):
            if obstacleGrid[m-1][j]:
                break
            dp[m-1][j] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]
# @lc code=end

