/*
 * @lc app=leetcode.cn id=239 lang=javascript
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    var queue = [];
    var res = [];
    for (var i=0; i<nums.length; i++) {
        if (queue.length==0) {
            queue.push(i);
        } else {
            if (queue[0] < i-k+1) {
                queue.shift();
            }
            while (queue.length>0 && nums[i] > nums[queue[queue.length-1]]) {
                queue.pop();
            }
            queue.push(i);
        }

        if (i>=k-1) {
            res.push(nums[queue[0]]);
        }
    }
    return res;
};
// @lc code=end

