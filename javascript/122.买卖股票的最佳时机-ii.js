/*
 * @lc app=leetcode.cn id=122 lang=javascript
 *
 * [122] 买卖股票的最佳时机 II
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    var maxres = 0;
    var min = prices[0];
    for (var price of prices) {
        if (price > min) {
            maxres += price-min; 
        }
        min = price;
    }
    return maxres;
};
// @lc code=end

