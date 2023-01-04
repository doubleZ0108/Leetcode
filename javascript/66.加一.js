/*
 * @lc app=leetcode.cn id=66 lang=javascript
 *
 * [66] 加一
 */

// @lc code=start
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    digits = digits.reverse();
    for (var i=0; i<digits.length; i++) {
        if (digits[i] != 9) { 
            digits[i]++;
            break;
        } else {
            digits[i] = 0;
        }
    }
    if (digits[digits.length-1] == 0) {
        digits.push(1);
    }
    return digits.reverse();
};
// @lc code=end

