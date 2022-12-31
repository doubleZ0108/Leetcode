#
# @lc app=leetcode.cn id=934 lang=python
#
# [934] 最短的桥
#

# @lc code=start
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)

        def DFS(x, y):
            if x<0 or y<0 or x>N-1 or y>N-1: return
            if grid[x][y] != 1: return
            if grid[x][y] == 1:
                grid[x][y] = 2
                S.add((x, y))
            DFS(x+1, y)
            DFS(x-1, y)
            DFS(x, y+1)
            DFS(x, y-1)

        def BFS():
            queue = []
            visited = set()
            for s in S:
                queue.append((s,0))
                visited.add(s)
            while queue:
                (i, j), step = queue.pop(0)
                if grid[i][j] == 1: return step-1
                for x, y in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                    if x>=0 and y>=0 and x<=N-1 and y<=N-1:
                        if (x,y) not in visited:
                            visited.add((x,y))
                            queue.append(((x,y),step+1))
        
        S = set()
        flag = False
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    DFS(i, j)
                    flag = True
                    break
            if flag: break
        
        return BFS()
# @lc code=end

