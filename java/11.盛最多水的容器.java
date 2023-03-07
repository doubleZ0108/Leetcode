/*
 * @lc app=leetcode.cn id=11 lang=java
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
class Solution {
    public int maxArea(int[] height) {
        int left=0, right=height.length-1;
        int res = (right-left)*Math.min(height[left], height[right]);
        while (left < right) {
            if (height[left] < height[right]) {
                ++left;
            } else {
                --right;
            }
            res = Math.max(res, (right-left)*Math.min(height[left], height[right]));
        }
        return res;
    }
}
// @lc code=end

