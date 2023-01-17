/*
 * @lc app=leetcode.cn id=746 lang=javascript
 *
 * [746] 使用最小花费爬楼梯
 */

// @lc code=start
/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    var dp = new Array(cost.length).fill(Infinity);
    dp[0] = cost[0];
    dp[1] = cost[1];

    for (var i=2; i<cost.length; i++) {
        dp[i] = Math.min(dp[i-1], dp[i-2]) + cost[i];
    }
    return Math.min(dp[cost.length-1], dp[cost.length-2]);
};
// @lc code=end

