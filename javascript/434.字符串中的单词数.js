/*
 * @lc app=leetcode.cn id=434 lang=javascript
 *
 * [434] 字符串中的单词数
 * 
 * 解法1(T30% S84%)：不能简单分割空格就返回，如果是很多空格在一起划分完会得到一个全是空格的字符，他们跑trim()就会得到空字符，要把这些filter()掉
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
    return s.split(" ").filter(s => s.trim()!="").length;
};
// @lc code=end

