/*
 * @lc app=leetcode.cn id=189 lang=javascript
 *
 * [189] 轮转数组
 * 
 * 注意题目说的in-place，因此不太能用库函数，因为他们会得到新列表
 * 另外初始k要取余降低复杂度
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    if (nums.length == 1) { return nums;} 
    k %= nums.length;
    
    for (var i=0,j=nums.length-1; i<j; i++,j--) {
        var tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    for (var i=0,j=k-1; i<j; i++,j--) {
        var tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    for (var i=k,j=nums.length-1; i<j; i++,j--) {
        var tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
};
// @lc code=end

