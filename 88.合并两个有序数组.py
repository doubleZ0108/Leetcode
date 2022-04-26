#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#
# 解法1(T95% S56%)：题是不难的，只是逻辑有点绕，不同于合并有序链表，题目中说明要直接在nums1上修改，因此不能开辟一个新的空数组不断append那种经典的做法。但思路还是双指针，首先要判断i指针指的位置是不是有效数据（i-j<m，因为i如果指到后面预留的0，很可能它比j的元素小）；如果i指针元素小那很好，直接往后移一位就可以（因为结果就保存在nums1里），如果j指针元素小，那就将nums1后面的元素依次往后移动一位，再把j元素放到当前位置
#   这题的难点就在于依次移动时的下标边界，以及要判断i指针是不是在nums1的有效数值内

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while j<n:
            if i-j<m:
                if nums1[i]<=nums2[j]:
                    i += 1
                else:
                    for k in range(m+j-1, i-1, -1):
                        nums1[k+1] = nums1[k]
                    nums1[i] = nums2[j]
                    i += 1
                    j += 1
            else:
                nums1[i] = nums2[j]
                j += 1
                i += 1
# @lc code=end

