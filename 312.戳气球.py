#
# @lc app=leetcode.cn id=312 lang=python
#
# [312] 戳气球
#
# 解法1(T81% S68%): 动态规划（加一层循环），`dp[i][j]`代表戳i～j之间（开区间｜不戳i和j）的球后得到的收益，最后要求的就是`dp[0][-1]`，比如最后一次戳k位置，那最后一次的收益就是`dp[i][k] + dp[k][j] + nums[i]*nums[j]*nums[k]`（把i～k之间的球按某种最优方式戳完，再把k～j之间的球戳完，最后戳k），那只要循环`k`保存最大值就可以找到全局最大值
#   同时要注意这道题dp的顺序要从后往前。如果从前往后：比如i从0开始循环到末尾，j从i+1开始循环到末尾，比如`dp[0][5]`这个值要一会才能求解到；因此要从后往前，i从最后往前走，j从i+1走到最后，k每次从i+1走到j，不断更新`dp[i][j]`

# @lc code=start
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]

        dp = [[0]*len(nums) for _ in range(len(nums))]

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1,len(nums)):
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[j]*nums[k])
        return dp[0][-1]
# @lc code=end

