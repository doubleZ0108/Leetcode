/*
 * @lc app=leetcode.cn id=476 lang=javascript
 *
 * [476] 数字的补数
 * 
 * 充分利用js的库函数完成
 */

// @lc code=start
/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    var num2 = num.toString(2);
    var num2_ = num2.split("").map(x => x=='0'?'1':'0').join("");
    return parseInt(num2_, 2);
};
// @lc code=end

