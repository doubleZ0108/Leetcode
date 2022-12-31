#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#
# 解法1(T78% S73%)：非常标准的二分搜索问题，而且还很全，如果没找到要返回其插入位置。按照二分查找经典方法做，首先设定left right指针，在while循环内部获取两指针的中心med，如果med的值等于target，则返回med的索引，否则进行二分缩减。最终如果没找到，此时left指向的位置就是应该顺序插入的位置

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            med = (left+right)//2
            if nums[med]==target:
                return med
            elif nums[med]<target:
                left = med + 1
            else:
                right = med - 1
        return left
# @lc code=end

