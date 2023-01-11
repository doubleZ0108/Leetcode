/*
 * @lc app=leetcode.cn id=219 lang=javascript
 *
 * [219] 存在重复元素 II
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    var map = new Map();
    for (var i=0; i<nums.length; i++) {
        if (map.has(nums[i])) {
            map.set(nums[i], map.get(nums[i]).concat(i));
        } else {
            map.set(nums[i], [i]);
        }
    }

    for (var arr of map.values()) {
        if (arr.length > 1) {
            arr.sort((a,b)=>(a-b));
            for (var i=1; i<arr.length; i++) {
                if (arr[i]-arr[i-1] <= k) {
                    return true;
                }
            }
        }
    }
    return false;
};
// @lc code=end

