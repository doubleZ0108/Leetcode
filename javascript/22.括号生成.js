/*
 * @lc app=leetcode.cn id=22 lang=javascript
 *
 * [22] 括号生成
 * 
 * 非常有趣，回溯法，回溯的核心是一次只解决一位，不要想着一次能很多位
 * 首先想好终止条件，然后设计参数传递，分情况考虑每次怎么能新引入一位，直到达到终止条件时结束
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    var res = [];
    var generator = function(part, left_now) {
        if (part.length == 2*n) {
            res.push(part);
            return;
        }
        if (part.length - left_now == left_now) {
            generator(part+'(', left_now+1);
        } else {
            if (left_now < n) {
                generator(part+"(", left_now+1);
            }
            generator(part+')', left_now);
        }
    };
    generator("", 0);
    return res;
};
// @lc code=end

