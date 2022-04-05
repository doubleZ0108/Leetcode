#
# @lc app=leetcode.cn id=136 lang=python
#
# [136] 只出现一次的数字
#
# 解法1(T92% S65%): 异或操作，数组中全部元素的异或结果即为数组中只出现一次的数
#   a @ a = 0
#   a @ 0 = 0
#   要求N复杂度，不引入额外内存消耗

from functools import reduce
# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y: x^y, nums)

    def otherSolution(self, nums):
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans
# @lc code=end

