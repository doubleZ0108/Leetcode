#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#
# 解法1(T45% S22%)：排序，遍历数组序号，如果数组元素不等于序号则返回当前位置，最终如果还没返回则返回数组长度
# 解法2(T95% S73%)：等差数列求和，一次遍历，常数空间 \frac{(0 + n) * (n-1)}{2} - sum(nums)

# @lc code=start
class Solution:
    # 解法2
    def missingNumber(self, nums: List[int]) -> int:
        return (0+len(nums))*(len(nums)+1)//2 - sum(nums)

    # 解法1
    def missingNumber1(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
# @lc code=end

