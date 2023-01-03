/*
 * @lc app=leetcode.cn id=53 lang=javascript
 *
 * [53] 最大子数组和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    if (nums.length == 1) { return nums[0]; }
    for (var i=1; i<nums.length; i++) {
        // 不单独构建一个dp数组，如果前一位是正数，则加上他肯定能使我变大
        if (nums[i-1] > 0) {
            nums[i] += nums[i-1];
        }
    }
    return Math.max(...nums);
};
// @lc code=end

