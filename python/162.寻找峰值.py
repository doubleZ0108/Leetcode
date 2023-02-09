#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
# 解法1(T73% S22%)：这题非常奇怪，说是要用$O(logN)$的算法实现，但只要一次遍历找到一个数比前一个数大比后一个数也大即可。极端来讲，直接返回数组全局最大值的下标也可
# 解法2：但毕竟说了要求，肯定是二分的思路，简单来说应该就是从中间点开始，哪边是上坡就往哪边走，不断缩小范围直到走到一个山顶即可

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if nums[1]<nums[0]: return 0
        if nums[len(nums)-2]<nums[len(nums)-1]: return len(nums)-1

        for i in range(1, len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
# @lc code=end

