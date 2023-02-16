#
# @lc app=leetcode.cn id=1154 lang=python
#
# [2341] 数组能形成多少数对
#
# 解法1(T70% S22%)：首先对数组排序，这样相同的元素就能聚集在一起，通过两个变量cnt和remain保存结果，如果nums[i+1]==nums[i]，则找到一个数对；否则nums[i]将会被剩下，根据两种情况更新变量和下标即可

# @lc code=start
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        cnt = 0
        remain = 0
        i = 0
        while i<len(nums):
            if i+1<len(nums) and nums[i+1]==nums[i]:
                cnt += 1
                i += 2
            else:
                remain += 1
                i += 1
        return [cnt, remain]
# @lc code=end