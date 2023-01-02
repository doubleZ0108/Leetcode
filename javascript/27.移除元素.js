/*
 * @lc app=leetcode.cn id=27 lang=javascript
 *
 * [27] 移除元素
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    if (nums.length == 0) { return 0; }
    if (nums.length == 1) {
        if (nums[0] == val) { return 0; }
        else { return 1; }
    }

    var backNum = 0;
    var i=0;
    while (i<=nums.length - backNum - 1) {  // 注意这个=
        if (nums[i] == val) {
            var tmp = nums[i];
            nums[i] = nums[nums.length - backNum - 1];
            nums[nums.length - backNum - 1] = tmp;
            backNum++;
        } else {
            i++;
        }
    }
    return i;
};
// @lc code=end

