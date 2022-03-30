#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] 三角形最小路径和
#
# 解法1(T55% S22%): 动态规划
# dp[i][j]：从顶点走到(i,j)的最短路径长
# 转移方程：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + t[i][j]
# 初始化：dp[0][0] = t[0][0]
# 目标：min(dp[0])
#     要注意下标索引不越界，在找上层元素时要防止越界，最终返回值也不要越界
#
#   改进1: 三角形这个结构是一层层的，当前层的传递只跟上一层有关，因此只需要n维的两个数组进行dp即可，空间复杂度降到O(N)
#   改进2(T83% S66%): 直接用原数组进行动态规划，不需要开辟新空间O(1)

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i-1][min(j,len(triangle[i-1])-1)], triangle[i-1][max(j-1,0)]) + triangle[i][j]

        return min(triangle[len(triangle)-1])

    def otherSolution(self, triangle):
        # 解法1
        n = len(triangle)
        dp = []
        for row in triangle:
            dp.append([0 for _ in range(len(row))])
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(len(triangle[i])):
                    dp[i][j] = min(dp[i-1][min(j,len(triangle[i-1])-1)], dp[i-1][max(j-1,0)]) + triangle[i][j]


        return min(dp[n-1])
        
Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
# @lc code=end

