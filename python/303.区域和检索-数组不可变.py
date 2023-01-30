#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
# 解法1(T7% S76%)：因为每次计算的区域都跟上一次没关系，所以还是得重新计算
#
# ✨解法2(T82% S62)：前缀和，数组不需要保存原来的数字，因为只需要计算范围内的求和，因此初始化时就利用dp的思想一次累加之前的所有元素到这位，求范围内的和时直接用right位置到求和 - (left-1)位置的求和即可

# @lc code=start
# 解法2
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i-1]


    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.nums[right]
        else:
            return self.nums[right]-self.nums[left-1]


# 解法1
class NumArray1:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(left, right+1):
            res += self.nums[i]
        return res



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

