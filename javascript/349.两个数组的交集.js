/*
 * @lc app=leetcode.cn id=349 lang=javascript
 *
 * [349] 两个数组的交集
 * 
 * js 集合语法比较原始
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    var set1 = new Set(nums1);
    var set2 = new Set(nums2);
    return [...set1].filter(x => set2.has(x));
};
// @lc code=end

