#
# @lc app=leetcode.cn id=847 lang=python
#
# [847] 访问所有节点的最短路径
#
# 解法1(超时)：因为所有边的长度都为1，因此对于无权无向图的遍历可以采用广度优先遍历。因为题目要求可以从任意节点出发，因此就将每个节点作为起始点分别进行广度优先遍历，且因为要遍历到所有节点，因此在常规的`(node, cost)` 元组基础上还要加加一个`traveled`数组记录每个点当前是否被遍历。
# 
#   改进1(T5% S85%)：这么做超时的主要问题是因为`traveled`是数组，没法hash，因此无法使用visited记录`(node, traveled)`是否出现过减小搜索空间。解决办法是将这个数组变为字符串 → 更进一步可以变为二进制字符串 → 又可以用一位十进制数表示，这样既可以hash，又进行了状态压缩。具体来说，
#       如果十进制数 == $2^N - 1$则代表所有节点都被访问到了，具体实现`if traveled == (1 << N) - 1:`
#       初始化为出发节点的二进制对应的十进制，`1<<start`（左移$i$位代表$\times 2^i$）
#       记录traveled信息的增加，`traveled_ = traveled | (1 << dst)`
#
#   改进2(T18% S33%)：也可以把所有点作为起点都压入同一个队列中然后一起做（替代外层循环），只要找到一个traveled全覆盖的就可以终止返回了

# @lc code=start
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        # 解法1 改进1
        minCost = 1e06
        for start in range(len(graph)): # 分别把每个点作为起始
            queue = [(start, 0, 1<<start)]
            visited = set((start, 1<<start))

            while queue:
                src, cost, traveled = queue.pop(0)
                if traveled == (1 << len(graph)) - 1:
                    minCost = min(minCost, cost)
                    break
                for dst in graph[src]:
                    traveled_ = traveled | (1 << dst)
                    if (dst, traveled_) not in visited:
                        queue.append((dst, cost+1, traveled_))
                        visited.add((dst, traveled_))

        return minCost


    def otherSolution(self, graph):
        # 解法1 改进2
        queue = [(start, 0, 1<<start) for start in range(len(graph))]
        visited = set((start, 1<<start) for start in range(len(graph)))

        while queue:
            src, cost, traveled = queue.pop(0)
            if traveled == (1 << len(graph)) - 1:
                return cost
            for dst in graph[src]:
                traveled_ = traveled | (1 << dst)
                if (dst, traveled_) not in visited:
                    queue.append((dst, cost+1, traveled_))
                    visited.add((dst, traveled_))


        # 解法1(超时)
        minCost = 1e06
        for start in range(len(graph)): # 分别把每个点作为起始
            queue = [(start, 0, [0 for _ in range(len(graph))])]
            queue[0][-1][start] = 1

            while queue:
                src, cost, traveled = queue.pop(0)
                if 0 not in traveled: 
                    minCost = min(minCost, cost)
                    break
                for dst in graph[src]:
                    traveled_ = traveled.copy()
                    traveled_[dst] = 1
                    queue.append((dst, cost+1, traveled_))

        return minCost

Solution().shortestPathLength([[2,3],[7],[0,6],[0,4,7],[3,8],[7],[2],[5,3,1],[4]])
# @lc code=end

