/*
 * @lc app=leetcode.cn id=12 lang=javascript
 *
 * [12] 整数转罗马数字
 */

// @lc code=start
/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    var res = "";

    while (num >= 1000) {
        res = res + "M";
        num -= 1000;
    }
    if (num >= 900) {
        res = res + "CM";
        num -= 900;
    }
    if (num >= 500) {
        res = res + "D";
        num -= 500;
    }
    if (num >= 400) {
        res = res + "CD";
        num -= 400;
    }
    while (num >= 100) {
        res = res + "C";
        num -= 100;
    }
    if (num >= 90) {
        res = res + "XC";
        num -= 90;
    }
    if (num >= 50) {
        res = res + "L";
        num -= 50;
    }
    if (num >= 40) {
        res = res + "XL";
        num -= 40;
    }
    while (num >= 10) {
        res = res + "X";
        num -= 10;
    }
    if (num >= 9) {
        res = res + "IX";
        num -= 9;
    }
    if (num >= 5) {
        res = res + "V";
        num -= 5;
    }
    if (num >= 4) {
        res = res + "IV";
        num -= 4;
    }
    while (num) {
        res = res + "I";
        num -= 1;
    }
    return res;
};
// @lc code=end

