/*
 * @lc app=leetcode.cn id=15 lang=javascript
 *
 * [15] 三数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    var res = [];
    nums = nums.sort((a,b) => (a-b));
    var i=0;
    while (i<nums.length) {
        var j=i+1, k=nums.length-1;
        while (j<k) {
            var tmp = nums[i] + nums[j] + nums[k];
            if (tmp == 0) {
                res.push([nums[i], nums[j], nums[k]]);
                while (j<k && nums[j+1]==nums[j]) { j++; }
                while (j<k && nums[k-1]==nums[k]) { k--; }
                j++;
                k--;
            } else if (tmp < 0) {
                while (j<k && nums[j+1]==nums[j]) { j++; }
                j++;
            } else {
                while (j<k && nums[k-1]==nums[k]) { k--; }
                k--;
            }
        }
        while (i<nums.length && nums[i+1]==nums[i]) { i++; }
        i++;
    }

    return res;
};
// @lc code=end

