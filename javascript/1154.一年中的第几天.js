/*
 * @lc app=leetcode.cn id=1154 lang=javascript
 *
 * [1154] 一年中的第几天
 */

// @lc code=start
/**
 * @param {string} date
 * @return {number}
 */
var dayOfYear = function(date) {
    var year = date.slice(0, 4);
    return (new Date(date) - new Date(year+"-01-01")) / 1000/60/60/24 + 1;
};
// @lc code=end

