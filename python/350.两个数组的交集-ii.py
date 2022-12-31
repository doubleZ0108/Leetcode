#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] 两个数组的交集 II
#
# 解法1(T85% S67%)：这题比上一题还更简单，直接双指针。首先排序，然后双指针同时遍历，如果指向相同则添加到结果中，否则让指向小的那个后移一位即可

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]: j += 1
            else: i += 1
        return res
# @lc code=end

