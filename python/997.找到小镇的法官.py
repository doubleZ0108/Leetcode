#
# @lc app=leetcode.cn id=997 lang=python
#
# [997] 找到小镇的法官
#
# 解法1(T84% S85%)：本质是图的问题。记录每个节点的入度和出度，最终找是否有节点的入度==节点总数-1 & 这个节点的出度==0 → 他受到其他所有人信任 & 他不信任任何人

# @lc code=start
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        graph = [[0,0] for _ in range(n+1)]
        for (a,b) in trust:
            graph[a][0] += 1
            graph[b][1] += 1
        for i in range(1, n+1):
            if graph[i][0] == 0 and graph[i][1] == n-1: return i
        return -1
# @lc code=end

