#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#
# 解法1(T47% S97%)：非常标准的数组查找题，外层循环遍历nums1的每个元素，内层循环依次找每个num1[i]下一个更大元素，可以直接通过数组的index()定位到元素的位置，往后找到nums2数组结尾即可

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1 for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]), len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        return res
# @lc code=end

