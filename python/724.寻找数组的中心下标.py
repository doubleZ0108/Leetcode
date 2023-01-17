#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#
# 解法1(T52% S84%)：可以视为最简单的滑窗问题，即窗口尺寸固定为1，此时问题简化为一个简单的双指针问题，left记录当前下标左边元素的和，right记录右边的和+当前元素，下标从0开始不断向后移动，如果发现left == right-nums[i]，则找到了满足题设条件的下标，否则该下标往后移动一位，同时更新left和right值
#
# 解法2：双重循环，外层从左到右移动下标，内层计算左右的值，如果和相等则返回，但很明显没有利用下标一位一位移动这个特性，增加了很多无谓的求和计算

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        idx = 0
        left, right_ = 0, sum(nums)

        while idx < len(nums):
            if left == right_-nums[idx]:
                return idx
            else:
                left += nums[idx]
                right_ -= nums[idx]
                idx += 1

        return -1
# @lc code=end

