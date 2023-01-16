/*
 * @lc app=leetcode.cn id=682 lang=javascript
 *
 * [682] 棒球比赛
 */

// @lc code=start
/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
    var stack = [];
    for (var op of operations) {
        switch (op) {
            case '+':
                stack.push(stack[stack.length-1] + stack[stack.length-2]);
                break;
            case 'C': 
                stack.pop();
                break;
            case 'D':
                stack.push(stack[stack.length-1] * 2);
                break;
            default:
                stack.push(parseInt(op));
        }
    }
    stack.push(0);
    stack.push(0);
    return stack.reduce((a, b) => a+b);
};
// @lc code=end

