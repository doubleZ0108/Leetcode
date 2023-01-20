/*
 * @lc app=leetcode.cn id=787 lang=javascript
 *
 * [787] K 站中转内最便宜的航班
 * 
 * 通过memo来缓存(当前位置，剩余步数)的最小值
 * 不需要visited集合
 */

// @lc code=start
/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, k) {
    var memo = Array.from(new Array(n), ()=>new Array(k+1).fill(-1));   // 注意这个k要+1
    var travel = function(s, remain) {
        if (s==dst) { return 0; }
        if (remain < 0) { return Infinity; }
        if (memo[s][remain]!=-1) { return memo[s][remain]; }

        var minCost = Infinity;
        for (var flight of flights) {
            if (s == flight[0]) {
                var cost = travel(flight[1], remain-1) + flight[2];
                minCost = Math.min(minCost, cost);
            }
        }
        memo[s][remain] = minCost;
        return minCost;
    }

    var res = travel(src, k);
    return res<Infinity ? res : -1;
};
// @lc code=end

