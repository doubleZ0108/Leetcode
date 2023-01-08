/*
 * @lc app=leetcode.cn id=128 lang=javascript
 *
 * [128] 最长连续序列
 * 
 * 解法2(JS T58% S25%): 先将数组转为集合set实现去重，再对所有非重复数字(set.keys())排序，然后通过动态规划来求解，如果前一位数字+1==当前数字，则dp[i]=dp[i-1]+1，最终返回最大的dp值即是长的连续序列长度
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if (nums.length<=1) { return nums.length; }

    var set = new Set(nums);
    var keys = [...set.keys()].sort((a,b)=>(a-b));
    var dp = new Array(keys.length).fill(1);
    for (var i=1; i<dp.length; i++) {
        if (keys[i-1]+1==keys[i]) {
            dp[i] = dp[i-1]+1;
        }
    }
    return Math.max(...dp);
};
// @lc code=end

