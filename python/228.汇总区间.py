#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
# 解法1(T86% S58%)：很典型的while双重循环的问题，站在某一点i上，不断向后看j，如果j+1元素始终是j元素的+1则不断往后走，它们可以合并成一个区间，i也可以直接跳到下一位；否则只有一个元素自己，i递增1

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        res = []
        while i<len(nums):
            j = i
            while j+1<len(nums) and nums[j+1]==nums[j]+1:
                j += 1

            if j!=i:
                res.append(str(nums[i])+"->"+str(nums[j]))
                i = j+1
            else:
                res.append(str(nums[i]))
                i += 1
        return res
# @lc code=end

