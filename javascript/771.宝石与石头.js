/*
 * @lc app=leetcode.cn id=771 lang=javascript
 *
 * [771] 宝石与石头
 * 
 * 解法1(JS 15% S78%)：先将jewels字符串划分成一个个字符，然后变为集合或哈希表（加速查找），一个一个石头字符看，如果在集合中则结果递增
 */

// @lc code=start
/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    var jewels_set = new Set(jewels.split(""));
    var res = 0;
    for (var stone of stones) {
        if (jewels_set.has(stone)) {
            res++;
        }
    }
    return res;
};
// @lc code=end

