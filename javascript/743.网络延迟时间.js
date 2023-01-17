/*
 * @lc app=leetcode.cn id=743 lang=javascript
 *
 * [743] 网络延迟时间
 */

// @lc code=start
/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function(times, n, k) {
    var costs = new Array(n+1).fill(Infinity);
    costs[k] = 0;
    var queue = [[k, 0]];
    var visited = new Set([k]);

    while (queue.length) {
        var data = queue.shift();
        var node=data[0], cost=data[1];
        for (var time of times) {
            var u=time[0], v=time[1], w=time[2];
            if (u == node && cost+w<costs[v]) {
                costs[v] = cost+w;
                if (!visited.has(v)) {
                    queue.push([v, costs[v]]);
                }
            }
        }
    }
    costs = costs.slice(1);
    if (costs.includes(Infinity)) {
        return -1;
    } else {
        return Math.max(...costs);
    }
};
// @lc code=end

