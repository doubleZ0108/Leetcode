#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# 解法1(T74% S26%)：好久没写深搜，偶尔写一次感觉好好玩。这种岛屿搜索的问题思路都很统一，我们循环数组，当看到一个1时，从这位开始深搜并把相邻岛屿标记成2，这样就找到了一个岛屿并把它跟其他岛屿区分开了，然后再往下循环即可。需要注意的是我们只需要一次二重循环就好，不需要再在二重循环外添加一重while True，必须当某次遍历没遇到任何1才认为把所有岛屿找全了，因为我们是从上往下从左往右依次遍历，如果找到了一个1并把与它相连的都变成了2，那么剩下的1一定在二位遍历的后面，要不然早就从这位出发深搜了

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def deepin(i, j):
            if i<0 or j<0 or i>m-1 or j>n-1 or grid[i][j]!='1': return
            grid[i][j] = '2'
            deepin(i+1, j)
            deepin(i-1, j)
            deepin(i, j-1)
            deepin(i, j+1)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    deepin(i, j)
                    flag = True
        return res
# @lc code=end

