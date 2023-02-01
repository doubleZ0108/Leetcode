#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# 解法1(T83% S98%)：直接调用python库函数 itertools.permutations(nums, len(nums))

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums, len(nums)))
# @lc code=end

