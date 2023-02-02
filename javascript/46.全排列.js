/*
 * @lc app=leetcode.cn id=46 lang=javascript
 *
 * [46] 全排列
 * 
 * 解法21(JS T17% S5%)：回溯，参数分别为parts数组和visited集合，当parts的长度等于原数组长度则添加到结果中，visited用于存储哪些数字已经用过了，从原数组中排除这些用过的，就是当前位可以添加并继续递归的
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    var res = [];
    var deepin = function(parts, visited) {
        if (parts.length == nums.length) {
            res.push(parts);
            return;
        }
        
        for (var item of [...nums].filter(x => !new Set(visited).has(x))) {
            deepin(parts.concat(item), visited.concat(item));
        }
    };
    deepin([], []);
    return res;
};
// @lc code=end

