#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
# 解法1(T36% S5%)：标准的一维动态规划问题，新开辟一个dp数组初始化每个位置的最长连续序列长度都是1，从下标1开始循环，如果nums[i]>nums[i-1]，则dp[i] = dp[i-1]+1，最后返回dp数组的最大值

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)
# @lc code=end

