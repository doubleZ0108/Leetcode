#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#
# 解法1(超时)：两次循环暴力解。每个位置都向左向右分别看每个柱子，计算（当前宽度*最小高度）的面积，更新最大面积
# 
# 解法2(T63% S86%)：双指针，经典面试题。首先两指针分别指向两边界，此时相当于把最左最右作为容器的边界，计算此时的最大面积（短板效应求），然后判断左柱和右柱谁更小，把更小的柱子移动一位（左→右 右→左），相当与更新了我认为可能的容器边界，这个边界里可能存在这更多的面积。进一步思考为什么会这样呢？面积=高*宽，每移动柱子相当于让宽度-1，为了获得更大的面积我们肯定希望移动后高度可以增加，这样面积才有可能填补宽度损失的1。而为什么要移动短柱呢？因为移动短柱位置后很可能新位置是更高的柱子，才可能让总面积更高。

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        themaxArea = 0
        left, right = 0, len(height)-1
        while left < right:
            themaxArea = max(themaxArea, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]: left += 1
            else: right -= 1
        return themaxArea

    def otherSolution(self, height):
        themaxArea = 0
        for idx in range(len(height)):
            for left in range(0, idx):
                themaxArea = max(themaxArea, (idx-left)*min(height[left],height[idx]))
            for right in range(idx+1, len(height)):
                themaxArea = max(themaxArea, (right-idx)*min(height[idx],height[right]))
        return themaxArea
# @lc code=end

