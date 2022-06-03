#
# @lc app=leetcode.cn id=349 lang=python
#
# [349] 两个数组的交集
#
# 解法1(T60% S83%)：直接调用库函数的`set()` 首先将两个数组通过集合去重，然后通过i`ntersection()`取两个集合的交集，最后转换为列表返回
# 
# 解法2(T60% S46%)：双指针。首先将两数组排序，然后双指针分别指向两数组的开始，如果当前指针指向数字和结果的最后一位一样则循环跳过这些位（注意防止数组越界），然后判断两指针指向，如果相等则添加到结果中，否则让指向数字小的指针往后移动一位

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
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
            if len(res) > 0:
                while i<len(nums1) and nums1[i]==res[-1]: i += 1
                while j<len(nums2) and nums2[j]==res[-1]: j += 1

            if i>=len(nums1) or j>=len(nums2): break
            
            if nums1[i]==nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]: i += 1
            else: j += 1

        return res

    def otherSolution(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        return list(s1.intersection(s2))
# @lc code=end

