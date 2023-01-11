/*
 * @lc app=leetcode.cn id=217 lang=javascript
 *
 * [217] 存在重复元素
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    nums.sort((a, b) => a-b);
    for (var i=1; i<nums.length; i++) {
        if (nums[i] == nums[i-1]) {
            return true;
        }
    }
    return false;
};
// @lc code=end

