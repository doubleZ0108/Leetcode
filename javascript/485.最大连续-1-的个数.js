/*
 * @lc app=leetcode.cn id=485 lang=javascript
 *
 * [485] 最大连续 1 的个数
 * 
 * 解法1(T44% S96%)：非常经典的动态规划问题，直接在原数组中更新，如果前一位和当前一位都不是0，则将前一位的值直接加到该位上，达到累积1的作用，最后返回数组中的最大值就是连续1的个数
 *   改进：通过一个变量存储并更新最大值，可以避免第二次一重循环找最大值
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    for (var i=1; i<nums.length; i++) {
        if (nums[i-1]!=0 && nums[i]!=0) {
            nums[i] += nums[i-1];
        }
    }
    return Math.max(...nums);
};
// @lc code=end

