/*
 * @lc app=leetcode.cn id=896 lang=javascript
 *
 * [896] 单调数列
 * 
 * 解法1(T80% S60%)：就是不想写两次循环，可以用一次完整的循环来判断，首先排除边界线条件，然后找到第一个相邻但不相等的元素，记录nums[i]-nums[i-1]的值为growordown，然后继续循环，同样还是排除相邻且相等的元素他们肯定单调，计算nums[i]-nums[i-1]和growordown的乘积，如果是单调的数列，那相邻元素相减应该同负同正，所以通过乘法就可以判断是否同号
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    if (nums.length <= 2) { return true; }
    var i=1;
    while (i<nums.length && nums[i]==nums[i-1]) {
        i++;
    } 
    var growordown = nums[i] - nums[i-1];
    for (i; i<nums.length; i++) {
        if (nums[i] == nums[i-1]) {
            continue;
        }
        if ((nums[i]-nums[i-1]) * growordown < 0) {
            return false;
        }
    }
    return true;
};
// @lc code=end

