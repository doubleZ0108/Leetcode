#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#
# 解法1(T78% S82%): 经典动态规划，跟求路径长度不同的是从右下角开始，最终的目标是求原点有多少种走法，转移方程直接把正右方和正下方的相加即可，初始化右边界和下边界都只有一种走法

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n==1:
            return 1

        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][n-1] = 1
        for j in range(n):
            dp[m-1][j] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
# @lc code=end

