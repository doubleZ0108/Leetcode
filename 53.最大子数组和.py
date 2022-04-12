#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子数组和
#
# 解法1(T50% S8%): 动态规划，`dp[i] = max(dp[i-1]+nums[i], nums[i])`
#   直观的思想就是每个位置都尽可能贪的跟前面多的加起来这样的得到的子数组就是最大的，但如果前面一个是负数，我跟他加上肯定就变小了不划算，也就意味着我要从头开始加了
# 
#   改进1(T23% S72%)：不开辟一整个dp数组，在原数组上进行dp传导，通过一个thismax变量找到最大值
#       python自带的max()会影响性能，还是直接用if判断快
# 
#   改进2(T88% S90%)：其实相当于只要上一位的dp值是正的，就把它融合进来，否则就重新开始累积

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 改进2
        thismax = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            if nums[i] > thismax:
                thismax = nums[i]

        return thismax

    def otherSolution(self, nums):
        # 解法2
        thismax = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
            thismax = max(thismax, nums[i])
        return thismax

        # 解法1
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)
# @lc code=end

