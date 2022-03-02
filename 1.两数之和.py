#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#
# 解法1(T21% S27%)：不排序，双重循环直接做
#   改进(T57% S67%)：python切片成两个数组，用in来判断是否在切片数组中，注意要在切片数组中找第二个数的位置，不能直接在原数组中找，因为可能有重复数字
# 
# 解法2(T70% S82%)：利用哈希表判断(target-当前数)是否在字典里，否则加入字典中（数字是key，位置是value）【空间换时间】
# 
# 解法3(T82% S98%)：先排序，用双指针一次遍历；找到两个数之后再在原数组中一次遍历获取下标

# @lc code=start

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 解法3
        arr = sorted(nums)
        i, j = 0, len(nums)-1
        while i<j:
            if arr[i] + arr[j] < target:
                i += 1
            elif arr[i] + arr[j] > target:
                j -= 1
            else:
                results = []
                for k, num in enumerate(nums):
                    if num in [arr[i], arr[j]]:
                        results.append(k)
                return results

    def otherSolutions(self, nums, target):
        # 解法1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        # 解法1 改进
        for i in range(len(nums)-1):
            remain = nums[i+1:]
            if target - nums[i] in remain:
                return [i, remain.index(target-nums[i])+i+1]    # 不能直接nums.index()，可能有重复数字

        # 解法2
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target-nums[i]], i]
            else:
                dict[nums[i]] = i

        
# @lc code=end

