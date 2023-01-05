/*
 * @lc app=leetcode.cn id=1803 lang=javascript
 *
 * [1803] 统计异或值在范围内的数对有多少
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
// 超时 59/63
var countPairs = function(nums, low, high) {
    var cnt = new Array(20001).fill(0);
    var min=2*20001, max = 0;
    for (var i in nums) {
        cnt[nums[i]]++;
        if (nums[i] < min) { min = nums[i]; }
        if (nums[i] > max) { max = nums[i]; }
    }

    var res = 0;
    for (var x=min; x<=max; x++) {
        if (cnt[x] > 0) {
            for (var t=low; t<=high; t++) {
                tmp = cnt[x] * cnt[x^t];
                if (tmp >=1 && tmp <= 20000) {
                    res += tmp;
                }
            }
        }
    }
    return Math.floor(res / 2);
};
// @lc code=end

