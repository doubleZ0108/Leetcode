/*
 * @lc app=leetcode.cn id=415 lang=javascript
 *
 * [415] 字符串相加
 */

// @lc code=start
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    var res = "";
    var bonus = 0;
    var i=num1.length-1, j=num2.length-1;
    while (i>-1 && j>-1) {
        var tmp = parseInt(num1[i])+parseInt(num2[j])+bonus;
        res = (tmp % 10) + res;
        bonus = Math.floor(tmp / 10);
        i--;
        j--;
    }
    while (i>-1) {
        var tmp = parseInt(num1[i])+bonus;
        res = (tmp % 10) + res;
        bonus = Math.floor(tmp / 10);
        i--;
    }
    while (j>-1) {
        var tmp = parseInt(num2[j])+bonus;
        res = (tmp % 10) + res;
        bonus = Math.floor(tmp / 10);
        j--;
    }
    if (bonus > 0) {
        res = bonus + res;
    }
    return res;
};
// @lc code=end

