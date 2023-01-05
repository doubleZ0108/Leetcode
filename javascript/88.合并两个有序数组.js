/*
 * @lc app=leetcode.cn id=88 lang=javascript
 *
 * [88] 合并两个有序数组
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
// 写起来还是有点烦的，这种in-place数组移动的题都有点考代码逻辑
var merge = function(nums1, m, nums2, n) {
    if (n==0) { return; }
    var i=0, j=0;
    var cnt = 0;
    while (i<m+n && j<n) {
        if (cnt == m) { break; }

        if (nums1[i] <= nums2[j]) {
            i++;
            cnt++;
        } else {
            for (var k=m+j; k>i; k--) {
                nums1[k] = nums1[k-1]
            }
            nums1[i] = nums2[j];
            i++;
            j++;
        }
    }
    while (j<n) {
        nums1[i] = nums2[j];
        j++;
        i++;
    }
};
// @lc code=end

