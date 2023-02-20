#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#
# 解法1(T18% S88%)：直接在原数组中模拟移动k次，每轮移动都从最后一行最后一列开始，不断向左向上移动，只要不是第一列的内容就直接将j-1的元素赋给j列，如果j==0则将上一行的最后元素进行填充，最后0行0列单独考虑就行

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for _ in range(k):
            tmp = grid[m-1][n-1]
            for i in range(m-1, -1, -1):
                for j in range(n-1, -1, -1):
                    if j == 0:
                        if i == 0:
                            grid[0][0] = tmp
                        else:
                            grid[i][j] = grid[i-1][-1]
                    else:
                        grid[i][j] = grid[i][j-1]
        return grid
# @lc code=end

