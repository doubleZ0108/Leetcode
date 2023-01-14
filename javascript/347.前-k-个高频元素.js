/*
 * @lc app=leetcode.cn id=347 lang=javascript
 *
 * [347] 前 K 个高频元素
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    var table = new Map();
    for (var num of nums) {
        if (!table.has(num)) {
            table.set(num, 1);
        } else {
            table.set(num, 1+table.get(num));
        }
    }
    var freq = [...table.entries()].sort((a,b)=>b[1]-a[1]);
    var res = [];
    for (var i=0; i<k; i++) {
        res.push(freq[i][0]);
    }
    return res;
};
// @lc code=end

