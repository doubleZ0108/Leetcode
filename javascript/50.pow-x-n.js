/*
 * @lc app=leetcode.cn id=50 lang=javascript
 *
 * [50] Pow(x, n)
 */

// @lc code=start
/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if (n==0) { return 1; }
    else if (n % 2 != 0) {
        if (n < 0) {
            return 1 / (x * myPow(x, -n-1));
        }
        else {
            return x * myPow(x, n-1);
        }
    } else {
        var tmp = 0;
        if (n < 0) {
            tmp = 1 / myPow(x, Math.floor(-n/2));
        } else {
            tmp = myPow(x, Math.floor(n/2));
        }
        return tmp * tmp;
    }
};

// 循环快速幂根本记不住
var myPow2 = function(x, n) {
    var neg_sign = n<0;
    if (n<0) { n = -n; }
    var res = 1;
    while (n) {
        if (n % 2 == 1) {
            res *= x;
        }
        x *= x;
        n = Math.floor(n/2);
    }
    return neg_sign ? 1/res : res;
};
// @lc code=end

