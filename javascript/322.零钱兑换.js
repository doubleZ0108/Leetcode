/*
 * @lc app=leetcode.cn id=322 lang=javascript
 *
 * [322] 零钱兑换
 */

// @lc code=start
/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    if (amount == 0) { return 0; }

    coins.sort((a,b) => a-b);
    var dp = new Array(amount+1).fill(Infinity);
    for (var coin of coins) {
        dp[coin] = 1;
    }

    for (var i=1; i<=amount; i++) {
        if (dp[i] == 1) { continue; }
        for (var coin of coins) {
            if (coin > i) { break; }
            dp[i] = Math.min(dp[i], dp[i-coin]+1);
        }
    }
    return dp[amount]<Infinity? dp[amount] : -1;
};
// @lc code=end

