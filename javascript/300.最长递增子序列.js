/*
 * @lc app=leetcode.cn id=300 lang=javascript
 *
 * [300] 最长递增子序列
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    var dp = new Array(nums.length).fill(1);
    for (var i=1; i<nums.length; i++) {
        var j=i-1;
        while (j>-1) {
            if (nums[j] < nums[i]) {
                dp[i] = Math.max(dp[i], dp[j]+1);
            }
            j--;
        }
    }
    return Math.max(...dp);
};
// @lc code=end

