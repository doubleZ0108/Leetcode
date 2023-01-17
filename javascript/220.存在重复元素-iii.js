/*
 * @lc app=leetcode.cn id=220 lang=javascript
 *
 * [220] 存在重复元素 III
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} indexDiff
 * @param {number} valueDiff
 * @return {boolean}
 */
var containsNearbyAlmostDuplicate = function(nums, indexDiff, valueDiff) {
    var T = Array.from(new Array(nums.length), () => new Array(2));
    for (var i=0; i<nums.length; i++) {
        T[i] = [nums[i], i];
    }
    T.sort((a, b) => (a[0] - b[0]));
    for (var i=0; i<T.length; i++) {
        var j=i+1;
        while (j<T.length && (Math.abs(T[i][1]-T[j][1])<=indexDiff || (Math.abs(T[i][0]-T[j][0]) <= valueDiff))) {
            if (Math.abs(T[i][1]-T[j][1])<=indexDiff && (Math.abs(T[i][0]-T[j][0]) <= valueDiff)) {
                return true;
            }
            j++;
        }
    }
    return false;
};
// @lc code=end

