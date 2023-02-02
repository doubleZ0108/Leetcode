#
# @lc app=leetcode.cn id=1129 lang=python3
#
# [1129] 颜色交替的最短路径
#
# 解法1(T15% S82%)：看起来很复杂，但本质就是标准的图中路径的问题，我们先回顾一下图中两点间最短路径的算法，两个数据结构queue和visited：queue每次弹出一个活节点，将与其相邻的节点进行更新，直到队列为空；visited用于记录哪些点访问过了，防止走重复路。那这道题有什么不同呢？每次颜色都要交换。那怎么办呢？将颜色信息也引入queue和visited，是否到达过某节点变为是否到达了某节点并且将以该颜色去下一个节点，queue保存的也不仅是节点和当前的路径长度，还要增加一个出发时的颜色。因为从0出发的时候什么颜色都可以，因此将0出发的两种可能颜色都作为初始，一起加入队列中，队列循环完自然会更新最短路径
#   本题代码可以继续优化，用01来标识两种颜色，将两个边数组放在一个二维数组中，这样1-color就能切换到另一种颜色中，不过现在的长代码更能看出来本质的思路就不改了

# @lc code=start
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [float('inf') for _ in range(n)]
        res[0] = 0

        queue = [(0, 0, 'r'), (0, 0, 'b')]
        visited = set([(0, 'r'), (0, 'b')])
        while queue:
            node, cost, color = queue.pop(0)
            if color == 'r':
                for start, end in redEdges:
                    if start == node and (end, 'b') not in visited:
                        res[end] = min(res[end], cost+1)
                        queue.append((end, cost+1, 'b'))
                        visited.add((end, 'b'))
            elif color == 'b':
                for start, end in blueEdges:
                    if start == node and (end, 'r') not in visited:
                        res[end] = min(res[end], cost+1)
                        queue.append((end, cost+1, 'r'))
                        visited.add((end, 'r'))
        
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] = -1
        return res
# @lc code=end

