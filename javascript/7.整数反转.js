/*
 * @lc app=leetcode.cn id=7 lang=javascript
 *
 * [7] 整数反转
 */

// @lc code=start
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    if (x>-10 && x<10) { return x; }

    var flag = x<0;
    if (flag) { x = -x; }
    var res = 0;
    while (x) {
        res *= 10;
        res += x % 10;
        x = Math.floor(x / 10);
    }

    if (flag) { res = -res; }

    if (res < -Math.pow(2, 31) || res > Math.pow(2, 31) - 1) { return 0; }
    return res;
};
// @lc code=end

