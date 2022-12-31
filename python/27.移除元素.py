#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#
# 解法1(T95% S45%)：想法不难，难在边界的判断上。设定左右指针，左指针发现等于val的时候，右指针不断向前找第一个不等于val的值，此时如果左右指针同位了，直接返回当前位置，否则左右指针元素对调继续遍历，最终返回左指针的位置

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] == val:
                while right>left and nums[right]==val:
                    right -= 1
                if right==left: return left
                nums[left], nums[right] = nums[right], nums[left]
            left += 1

        return left
# @lc code=end

