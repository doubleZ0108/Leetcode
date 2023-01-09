/*
 * @lc app=leetcode.cn id=136 lang=javascript
 *
 * [136] 只出现一次的数字
 * 
 * 异或的性质：a^a=0   a^0=a   a^b=c <=> a^c=b
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var only = 0;
    for (var num of nums) {
        only ^= num;
    }
    return only;
};
// @lc code=end

