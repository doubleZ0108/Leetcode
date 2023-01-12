/*
 * @lc app=leetcode.cn id=231 lang=javascript
 *
 * [231] 2 的幂
 */

// @lc code=start
/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if (n<=0) { return false; }
    if (n<=2) { return true; }
    return n == Math.pow(2, Math.floor(Math.log2(n)));
};
// @lc code=end

