/*
 * @lc app=leetcode.cn id=169 lang=javascript
 *
 * [169] 多数元素
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    var major = [];
    for (var num of nums) {
        if (major.length == 0 || num == major[0]) {
            major.push(num);
        } else {
            major.shift();
        }
    }
    return major[0];
};
// @lc code=end

