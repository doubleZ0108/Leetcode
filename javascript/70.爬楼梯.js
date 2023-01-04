/*
 * @lc app=leetcode.cn id=70 lang=javascript
 *
 * [70] 爬楼梯
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n<3) { return n;}
    var a=1, b=2;
    var res = 0;
    for (var i=2; i<n; i++) {
        res = a + b;
        a = b;
        b = res;
    }
    return res;
};
// @lc code=end

