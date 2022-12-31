#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#
# 解法1(暴力)：直接三重循环做
#   最后一个样例会超时
# 解法2(T48% S92%)：首先排序，对第一个数遍历，第二三个数可以用双指针来做
#   ✨双指针不一定要向折半查找那样，也可以一次只移一位，这样中间的所有数都会照顾到，复杂度也从平方→线性
#   改进1: 如果=target，直接终止
#   ✨改进2: 如果下一个数跟这一次一样，可以通过while将这些重复的枚举都省略掉

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        save = nums[0]+nums[1]+nums[2]
        nums.sort()
        i = 0
        while i < len(nums)-2:
            left, right = i+1, len(nums)-1
            while left < right:
                this = nums[i]+nums[left]+nums[right]
                # 改进1
                if this == target:
                    return this
                elif this > target:
                    # 改进2
                    while right-1 > left and nums[right-1]==nums[right]:
                        right -= 1
                    right -= 1
                else:
                    while left+1 < right and nums[left+1]==nums[left]:
                        left += 1
                    left += 1
                if abs(this - target) < abs(save - target):
                    save = this
            
            while i+1 < len(nums)-2 and nums[i+1]==nums[i]:
                i += 1
            i += 1
        
        return save

    def otherSolution(self, nums, target):
        # 解法1 暴力法
        save = -target if target!=0 else 10000
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    this = nums[i]+nums[j]+nums[k]
                    if this == target:
                        return target
                    elif abs(this - target) < abs(save - target):
                        save = this
# @lc code=end

