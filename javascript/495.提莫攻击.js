/*
 * @lc app=leetcode.cn id=495 lang=javascript
 *
 * [495] 提莫攻击
 * 
 * 解法1(T78% S96%)：一次循环攻击时间数组，如果i时间攻击的中毒要持续到i+1时间之后，那总时间只先递增两时间戳之差，将后半段时间的累加交给下一时刻，否则直接加上持续时间
 */

// @lc code=start
/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    var res = 0;
    for (var i=0; i<timeSeries.length; i++) {
        if (i+1<timeSeries.length && timeSeries[i]+duration-1 >= timeSeries[i+1]) {
            res += timeSeries[i+1] - timeSeries[i];
        } else {
            res += duration;
        }
    }
    return res;
};
// @lc code=end

