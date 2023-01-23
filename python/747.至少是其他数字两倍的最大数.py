#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#
# 解法1(T41% S55%)：直接利用python自带的库函数解决，因为题干说肯定存在唯一最大值，因此通过max()函数获取最大值，再通过index()函数获取最大值的下标，一次循环判断是否有数字的两倍比最大值还大，这里可以用any()配合列表生成式来做

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxidx = nums.index(max(nums))
        return -1 if any([2*num>nums[maxidx] for num in nums if num!=nums[maxidx]]) else maxidx
# @lc code=end

