#
# @lc app=leetcode.cn id=743 lang=python
#
# [743] 网络延迟时间
#
# 解法1(T7% S94%)：非常标准的一道Dijkstra最短路径，题目设计的也很巧妙。目标就是求起始点到所有点的最短路径中最长的那条，使用优先队列实现`queue.PriorityQueue`。首先初始化`pathTo`代表起始点到每个节点的距离为None（到自己的为0），然后初始化优先队列为起点，只要优先队列不空则一直循环；内层首先出队当前节点，在边集合中遍历，找到以当前节点为起点的边并更新目标节点的权重，再将目标节点加入优先队列；最终遍历一次`pathTo`，如果还有节点为None则代表起点无法遍历整张图，否则选取最大的值输出即可
#   改进1(T12% S80%)：添加`visited`，如果当前节点就在visited中则不用看了，在更新节点权重时如果目标节点在visited里也不用看了

# @lc code=start
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        pathTo = {node: None for node in range(1,n+1)}
        pathTo[k] = 0

        from queue import PriorityQueue
        pri_q = PriorityQueue()
        pri_q.put((0, k))

        visited = set()

        while not pri_q.empty():
            cost, node = pri_q.get()
            if node in visited: continue
            visited.add(node)

            for time in times:
                if time[0] == node and time[1] not in visited:
                    if pathTo[time[1]] is None or pathTo[time[1]] > cost+time[2]:
                        pathTo[time[1]] = cost + time[2] 
                        pri_q.put((pathTo[time[1]], time[1]))

        maxCost = 0
        for node, cost in pathTo.items():
            if cost is None: return -1
            maxCost = max(maxCost, cost)
        return maxCost
# @lc code=end

