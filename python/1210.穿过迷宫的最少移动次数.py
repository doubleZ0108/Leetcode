#
# @lc app=leetcode.cn id=1210 lang=python3
#
# [1210] 穿过迷宫的最少移动次数
#
# 解法1(T7% S97%)：一看走迷宫马上想到应该是动态规划，但这题的难点在于蛇有两个长度，蛇头蛇尾动来动去很麻烦，因此我们不妨只考虑蛇尾的位置，而将蛇头的位置转换为蛇的状态status，分别是水平和竖直，这样我们依然可以通过类二维dp数组来做，只不过数组的每一位有两种可能的status。将每种情况在纸上画出来然后写代码就好，需要注意的是，旋转的2种情况要在4种平移全结束之后再写，否则由于dp还没更新到(i,j)位置导致一直为Infinity

# @lc code=start
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[float('inf'), float('inf')] for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = 0

        for i in range(n):
            for j in range(n):
                if j+1<n and grid[i][j]==0 and grid[i][j+1]==0:
                    if i-1>-1:
                        dp[i][j][0] = min(dp[i][j][0], dp[i-1][j][0]+1)
                    if j-1>-1:
                        dp[i][j][0] = min(dp[i][j][0], dp[i][j-1][0]+1)
                    
                
                if i+1<n and grid[i][j]==0 and grid[i+1][j]==0:
                    if i-1>-1:
                        dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][1]+1)
                    if j-1>-1:
                        dp[i][j][1] = min(dp[i][j][1], dp[i][j-1][1]+1)


                if i+1<n and j+1<n and grid[i][j]==0 and grid[i][j+1]==0 and grid[i+1][j+1]==0:
                        dp[i][j][0] = min(dp[i][j][0], dp[i][j][1]+1)
                if j+1<n and i+1<n and grid[i][j]==0 and grid[i+1][j]==0 and grid[i+1][j+1]==0:
                    dp[i][j][1] = min(dp[i][j][1], dp[i][j][0]+1)

        return dp[n-1][n-2][0] if dp[n-1][n-2][0]<float('inf') else -1
# @lc code=end

