/*
 * @lc app=leetcode.cn id=58 lang=javascript
 *
 * [58] 最后一个单词的长度
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    var tokens = s.trimEnd().split(" ");
    return tokens[tokens.length-1].length;
};
// @lc code=end

