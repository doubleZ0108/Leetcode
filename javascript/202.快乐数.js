/*
 * @lc app=leetcode.cn id=202 lang=javascript
 *
 * [202] 快乐数
 */

// @lc code=start
/**
 * @param {number} n
 * @return {boolean}
 */
var cal = function(n) {
    var res = 0;
    while (n) {
        res += Math.pow(n%10, 2);
        n = Math.floor(n / 10);
    }
    return res;
};

var isHappy = function(n) {
    var set = new Set();
    while (!set.has(n)) {
        set.add(n);
        n = cal(n);
        console.log(n)
        if (n == 1) {
            return true;
        }
    }
    return false;
};
// @lc code=end

