/*
 * @lc app=leetcode.cn id=16 lang=java
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int res = nums[0]+nums[1]+nums[2];
        for (int i=0; i<nums.length-2; ++i) {
            int j=i+1, k=nums.length-1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == target) {
                    return target;
                } else if (sum < target) {
                    ++j;
                } else {
                    --k;
                }
                if (Math.abs(sum-target) < Math.abs(res-target)) {
                    res = sum;
                }
            }
        }
        return res;
    }
}
// @lc code=end

