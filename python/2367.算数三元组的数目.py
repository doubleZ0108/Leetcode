#
# @lc app=leetcode.cn id=2367 lang=python
#
# [2367] 算数三元组的数目
#
# 

# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                        res += 1
        return res
# @lc code=end