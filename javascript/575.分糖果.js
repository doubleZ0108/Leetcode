/*
 * @lc app=leetcode.cn id=575 lang=javascript
 *
 * [575] 分糖果
 * 
 * 解法1(T92% S72%)：利用集合对数组去重，返回数组长度/2和糖果种类二者的最小值
 */

// @lc code=start
/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    return Math.min(Math.floor(candyType.length/2), new Set(candyType).size);
};
// @lc code=end

