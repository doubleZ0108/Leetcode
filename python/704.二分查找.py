#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
# 解法1(T96% S29%)：直接使用语言自带的API，注意python讲字符串直接变为小写的是`.lower()`，toLowerCase()不是这么用的

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j =  mid - 1
        return -1
# @lc code=end

