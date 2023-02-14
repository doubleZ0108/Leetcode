#
# @lc app=leetcode.cn id=551 lang=python3
#
# [561] 数组拆分
#
# 解法1(T50% S45%)：有点像田忌赛马，因为是要取min()，所以每个数都要搭配一个尽可能小的数，稍微想一想，其实就是先排序，然后直接两两成对最经济合理，这样下标为偶数的这些数就是数对的最小值

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i, num in enumerate(nums):
            if i%2==0:
                res += num
        return res
# @lc code=end

