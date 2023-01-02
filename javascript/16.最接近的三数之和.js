/*
 * @lc app=leetcode.cn id=16 lang=javascript
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    var closest = nums.slice(0, 3).reduce((a, b) => a+b);
    nums = nums.sort((a, b) => a-b);
    for (var i=0; i<nums.length; i++) {
        var j=i+1, k=nums.length-1;
        while (j < k) {
            var tmp = nums[i]+nums[j]+nums[k];
            if (tmp == target) { return tmp; }
            if (Math.abs(tmp - target) < Math.abs(closest - target)) {
                closest = tmp;
            }
            if (tmp < target) { j++; }
            else { k--; }
        }
    }
    return closest;
};
// @lc code=end

