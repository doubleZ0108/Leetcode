/*
 * @lc app=leetcode.cn id=263 lang=javascript
 *
 * [263] 丑数
 */

// @lc code=start
/**
 * @param {number} n
 * @return {boolean}
 */
var isUgly = function(n) {
    while (n>=5 && n%5==0) {
        n /= 5;
    }
    while (n>=3 && n%3==0) {
        n /= 3;
    }
    while (n>=2 && n%2==0) {
        n /= 2;
    }

    return n==1;
};
// @lc code=end

