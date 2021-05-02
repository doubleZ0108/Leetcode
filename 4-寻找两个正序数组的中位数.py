#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        arr = []
        i, j = 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        arr += nums1[i:m]
        arr += nums2[j:n]
        # while i < m:
        #     arr.append(nums1[i])
        #     i += 1
        # while j < n:
        #     arr.append(nums2[j])
        #     j += 1

        arr_length = len(arr)
        if arr_length % 2:
            result = arr[arr_length // 2]
        else:
            result = (arr[arr_length // 2 - 1] + arr[arr_length // 2]) / 2
        
        return round(result, 5)
# @lc code=end

