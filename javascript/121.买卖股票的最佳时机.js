/*
 * @lc app=leetcode.cn id=121 lang=javascript
 *
 * [121] 买卖股票的最佳时机
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if (prices.length == 1) { return 0; }
    var minPrice = prices[0];
    var maxProfit = 0;
    for (var i=1; i<prices.length; i++) {
        minPrice = Math.min(minPrice, prices[i]);
        maxProfit = Math.max(maxProfit, prices[i]-minPrice);
    }
    return maxProfit;
};
// @lc code=end

