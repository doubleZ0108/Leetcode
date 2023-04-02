#
# @lc app=leetcode.cn id=1039 lang=python3
#
# [1039] 多边形三角剖分的最低得分
#
# 解法1(T96% S80%)：看题目明显是要不断尝试选最小值的，肯定不能直接暴力几重循环模拟，那肯定就是要动态规划了，比如对于4个顶点的多边形，在1号位置切还是在2号位置切，这明显是要在dp中插入一冲循环，用类似【戳气球】的思路来求解。dp[i][j]代表由顶点i～j组成的多边形的最小值，初始值为inf，且i+2>j的所有内容变为0，i+2==j的元素就直接组成了三角形最小值就是values[i]*values[i+1]*values[i+2] ，之后的转移过程就是对于i和j，从中间插入一个k，计算k划分成两个部份的和以及这个新引入的三角形的最小值。需要注意的是i要从后往前循环，因为j每次都是从i+2～n，如果后面没提前算完，可能会遇到非全局最小值

# @lc code=start
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        if n == 3:
            return reduce(lambda x, y: x*y, values)

        # dp = [[0]*n for _ in range(n)]
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, min(i+3, n)):
                dp[i][j] = values[i]*values[i+1]*values[i+2] if i+2==j else 0

        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+values[i]*values[k]*values[j])

        print(dp)
        return dp[0][n-1]
# @lc code=end

