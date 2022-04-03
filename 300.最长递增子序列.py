#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长递增子序列
#
# 解法1(T46% S30%): 一点点动态规划的思想但不完全是，当前一个字符能不能是最长增序列的一员取决于他之前有没有比他小的，到它的长度=之前比他小中最大的长度+1；最终返回的就是整个dp数组中最大的长度，复杂度是O(N^2)

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for _ in range(len(nums))]
        dp[0] = 1

        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
# @lc code=end

