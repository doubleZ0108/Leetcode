/*
 * @lc app=leetcode.cn id=367 lang=javascript
 *
 * [367] 有效的完全平方数
 */

// @lc code=start
/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    for (var i=1; i*i<=num; i++) {
        if (i*i==num) {
            return true;
        }
    }
    return false;
};
// @lc code=end

