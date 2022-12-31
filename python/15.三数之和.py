#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#
# 解法1(T10% S66%): 首先排序，迭代第一个数，后两个数通过双指针来降复杂度
#   改进1(T28% S93%): 做指针移动的时候，如果移完的数跟上一次是一样的，可以通过while跳过，同时还可以以此省略判断结果中是否有的in操作
#   改进2(T43% S93%): 如果最小的数都 >0，就可以提前终止了；如果最大的数还 <0，也可以提前终止了

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []

        nums.sort()
        if nums[0]>0 or nums[-1]<0:
            return []
        
        i = 0
        result = []
        while i<len(nums)-2 and nums[i]<=0:    # 改进2
            j, k = i+1, len(nums)-1
            while j < k:
                this = nums[i] + nums[j] + nums[k]
                if this == 0:
                    # if [nums[i], nums[j], nums[k]] not in result:
                    result.append([nums[i], nums[j], nums[k]])
                    while j+1<k and nums[j+1]==nums[j]:
                        j += 1
                    while k-1>j and nums[k-1]==nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
                    if nums[k]<=0:
                        continue
                elif this < 0:
                    # 改进1
                    while j+1<k and nums[j+1]==nums[j]:
                        j += 1
                    j += 1
                else:
                    while k-1>j and nums[k-1]==nums[k]:
                        k -= 1
                    k -= 1
                    # 改进2
                    if nums[k]<=0:
                        continue
            while i<len(nums)-2 and nums[i]<=0 and nums[i+1]==nums[i]:
                i += 1
            i += 1
        return result
# @lc code=end

