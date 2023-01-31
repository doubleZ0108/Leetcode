/*
 * @lc app=leetcode.cn id=414 lang=javascript
 *
 * [414] 第三大的数
 * 
 * 解法1(T66% S20%)：首先将数组转为集合去重，如果集合元素少于3个，则直接返回最大值；否则排序，直接返回下标为2的元素
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    var set = new Set(nums);
    if (set.size < 3) {
        return Math.max(...[...set]);
    } else {
        var li = [...set];
        li.sort((a, b) => b-a);
        return li[2];
    }
};
// @lc code=end

