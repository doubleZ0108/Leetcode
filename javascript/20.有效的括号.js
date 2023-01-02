/*
 * @lc app=leetcode.cn id=20 lang=javascript
 *
 * [20] 有效的括号
 */

// @lc code=start
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var stack = [];
    var table = { '(': ')', '{': '}', '[': ']'}
    for (var i in s) {
        if (Object.keys(table).includes(s[i])) {
            stack.push(s[i])
        } else {
            var top = stack.pop();
            if (table[top] != s[i]) { return false; }
        }
    }
    return stack.length==0;
};
// @lc code=end

