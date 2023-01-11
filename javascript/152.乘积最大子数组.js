/*
 * @lc app=leetcode.cn id=152 lang=javascript
 *
 * [152] 乘积最大子数组
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    var dp_min = [...nums];
    var dp_max = [...nums];

    for (var i=1; i<nums.length; i++) {
        dp_min[i] = Math.min(dp_min[i], dp_min[i-1]*nums[i], dp_max[i-1]*nums[i]);
        dp_max[i] = Math.max(dp_max[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i]);
    }
    return Math.max(...dp_max);
};

var maxProduct2 = function(nums) {
    var res = nums[0];
    var fromleft = 1;
    for (var i=0; i<nums.length; i++) {
        if (nums[i] == 0) {
            fromleft = 1;
            res = Math.max(res, 0);
        } else {
            fromleft *= nums[i];
            res = Math.max(res, fromleft);
        }
    }
    var fromright = 1;
    for (var j=nums.length-1; j>-1; j--) {
        if (nums[j] == 0) {
            fromright = 1;
            res = Math.max(res, 0);
        } else {
            fromright *= nums[j];
            res = Math.max(res, fromright);
        }
    }
    return res;
};
// @lc code=end

