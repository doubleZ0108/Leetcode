#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#
# 解法1(T91% S64%)：由于题目规模很小，因此直接按题意暴力做就可以，按照l和r进行数组切片，然后排序，再通过一重循环判断切片排序数组是否为等差数列即可

# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True

        res = []
        for l_, r_ in zip(l, r):
            parts = nums[l_:r_+1]
            parts.sort()
            res.append(check(parts))
        return res
# @lc code=end

