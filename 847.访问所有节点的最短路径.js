/*
 * @lc app=leetcode.cn id=847 lang=javascript
 *
 * [847] 访问所有节点的最短路径
 * 
 * 核心在于(node, cost, travel)的广度优先搜索
 * travel的位运算也很trick
 */

// @lc code=start
/**
 * @param {number[][]} graph
 * @return {number}
 */
var shortestPathLength = function(graph) {
    var n = graph.length;
    var minCost = Infinity;
    for (var start=0; start<n; start++) {
        var queue = [[start, 0, 1<<start]];
        var visited = Array.from(new Array(n), ()=>new Array(1<<n).fill(false));
        visited[start][1<<start] = true;

        while (queue) {
            var data = queue.shift();
            var from=data[0], cost=data[1], travel=data[2];
            if (travel == (1<<n)-1) {
                minCost = Math.min(minCost, cost);
                break;
            }

            for (var to of graph[from]) {
                var traveled_ = travel | (1<<to);
                if (!visited[to][traveled_]) {
                    queue.push([to, cost+1, traveled_]);
                    visited[to][traveled_] = true;
                }
            }
        }
    }
    return minCost;
};
// @lc code=end

