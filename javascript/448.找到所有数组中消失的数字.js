/*
 * @lc app=leetcode.cn id=448 lang=javascript
 *
 * [448] 找到所有数组中消失的数字
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    var sets = new Set(nums);
    var res = [];
    for (var i=1; i<=nums.length; i++) {
        if (!sets.has(i)) {
            res.push(i);
        }
    }
    return res;
};


// 注意数组里面那个嵌套也需要加abs，因为可能前面的某个人让它为负了
var findDisappearedNumbers2 = function(nums) {
    for (var i=0; i<nums.length; i++) {
        nums[Math.abs(nums[i])-1] = -Math.abs(nums[Math.abs(nums[i])-1]);
    }
    var res = [];
    for (var i=0; i<nums.length; i++) {
        if (nums[i] > 0) {
            res.push(i+1);
        }
    }
    return res;
};
// @lc code=end

