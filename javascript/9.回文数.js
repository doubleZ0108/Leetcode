/*
 * @lc app=leetcode.cn id=9 lang=javascript
 *
 * [9] 回文数
 */

// @lc code=start
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) { return false; }
    else if (x < 10) { return true; }

    var save = x;
    var tmp = 0;
    while (save) {
        tmp *= 10;
        tmp += save % 10;
        save = Math.floor(save / 10);
    }

    return tmp == x;
};

var isPalindrome2 = function(x) {
    x = x.toString()
    return x.split("").reverse().join("") == x;
};
// @lc code=end

