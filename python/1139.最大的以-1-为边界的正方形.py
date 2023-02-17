#
# @lc app=leetcode.cn id=1139 lang=python3
#
# [1139] 最大的以 1 为边界的正方形
#
# 解法1(T6% S99%)：直接暴力法来解决这个问题就好，当然还要稍微对复杂度优化一点。首先我们先写一个独立的函数判断以某个点为左上角起点，某个长度为边的正方形边界是否都为1，只需要横竖两重循环即可；有了这个函数我们就可以遍历grid的每个位置的每个长度了，当然有一些小技巧，因为是要求最大值，因此肯定从大往小遍历可能的变长，如果要遍历的变长比当前最大值还小就不用看了；另外在某个位置，最大的边长可能是当前位置距离右边界和下边界距离的最小值

# @lc code=start
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def issquare(x, y, l):
            for i in range(x, x+l):
                if grid[i][y]==0 or grid[i][y+l-1]==0:
                    return False
            for j in range(y, y+l):
                if grid[x][j]==0 or grid[x+l-1][j]==0:
                    return False
            return True

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxl = min(m-i, n-j)
                    for l in range(maxl, res-1, -1):
                        if issquare(i, j, l):
                            res = max(l, res)
                            break
        return res**2
# @lc code=end

