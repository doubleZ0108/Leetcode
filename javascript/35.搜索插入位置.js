/*
 * @lc app=leetcode.cn id=35 lang=javascript
 *
 * [35] 搜索插入位置
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    var i=0, j=nums.length-1;
    while (i<=j) {
        var mid = Math.floor((i + j) / 2);
        if (nums[mid] == target) { return mid; }
        else if (nums[mid] < target) { i++; }
        else { j--; }
    }
    return i;
};
// @lc code=end

