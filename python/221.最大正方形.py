#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# 解法1(超时 75/78)：二重循环每个1的位置，向外一层层的扩展正方形边的长度，只需要最外面一竖或者最外面一行为1就可以让该点为左上角点的正方形边长大1，找最大值即可
# 解法2(超时 76/78)：一个二维dp数组用于统计高的长度，类似于85题，再通过一重循环从右到左遍历长度，依次选取最小值的边作为正方形的边长
# 解法3(T34% S15%)：看题就是非常经典的二维动态规划求解法，可能自己想的总是太复杂总是要考虑一个一个的情况，而dp就是直接保存正方形的边长就可以，因此直接选取上/左/左上三个人里的最小值并扩展一个即可，可能自己对于这个还是不太熟

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [[0]*n for _ in range(m)]
        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                res = 1
        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                res = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                res = max(res,dp[i][j]**2)
        return res
# @lc code=end

