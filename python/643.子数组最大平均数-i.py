#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# 解法1(T89% S8%)：看这个数据规模如果直接二重循环做可能会超时，不如把题看成一个简单的滑窗问题，先算第一个k窗口内的和，每次循环一位时减去i-k元素的值，加上i元素的值，然后计算平均，并更新平均值的最大值

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cnt = 0
        for i in range(k):
            cnt += nums[i]
        avgmax = cnt / k
        for i in range(k, len(nums)):
            cnt = cnt - nums[i-k] + nums[i]
            avgmax = max(avgmax, cnt / k)
        return avgmax
# @lc code=end

