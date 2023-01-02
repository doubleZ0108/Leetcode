/*
 * @lc app=leetcode.cn id=26 lang=javascript
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length == 1) { return 1; }
    var backNum = 0;
    var i=1;
    while (nums[i]>=nums[i-1]) {
        if (nums[i] == nums[i-1]) {
            var back = nums[i];
            for (var j=i; j<nums.length-backNum; j++) {
                nums[j] = nums[j+1];
            }
            nums[nums.length-backNum] = back;
            backNum++;
        } else {
            i++;
        }
    }
    return i;
};
// @lc code=end

