/*
 * @lc app=leetcode.cn id=312 lang=javascript
 *
 * [312] 戳气球
 * 
 * 核心是i~j => j~k+k~j+戳k的奖励
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxCoins = function(nums) {
    nums.push(1);
    nums.unshift(1);
    var dp = Array.from(new Array(nums.length), ()=>new Array(nums.length).fill(0));
    for (var i=nums.length-1; i>-1; i--) {
        for (var j=i+1; j<nums.length; j++) {
            for (var k=i+1; k<j; k++) {
                dp[i][j] = Math.max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[j]*nums[k]);
            }
        }
    }
    return dp[0][nums.length-1];
};
// @lc code=end

