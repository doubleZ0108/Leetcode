/*
 * @lc app=leetcode.cn id=33 lang=javascript
 *
 * [33] 搜索旋转排序数组
 * 
 * 解法1(T47% S55%)：暂时想到的办法是找到数组断开的地方，将数组划分成两个，然后分别在两段里做二分搜索，将二分搜索打包成函数，向外暴露左右指针即可
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    var pivot = 0;
    while (pivot < nums.length && nums[pivot+1]>nums[pivot]) {
        pivot++;
    }
    
    var binarysearch = function(i, j) {
        while (i<=j) {
            var mid = Math.round((i+j) / 2);
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                i = mid + 1;
            } else {
                j = mid - 1;
            }
        }
        return -1;
    }

    var s1 = binarysearch(0, pivot);
    if (s1!=-1) {
        return s1;
    } else {
        var s2 = binarysearch(pivot+1, nums.length-1);
        if (s2 != -1) {
            return s2;
        }
    }
    return -1;
};
// @lc code=end

