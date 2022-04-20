#
# @lc app=leetcode.cn id=84 lang=python
#
# [84] 柱状图中最大的矩形
#
# 解法1(超时): 对于每根柱子，把他作为高，向左向右找第一个比他矮的就找到了宽，整体遍历一遍找最大的面积就解决了
# 
#   改进(T92% S58%)：每次都向左向右找比他小的，整体复杂度就是$O(N^2)$了 → **单调栈**：依次进，当进某一个的时候发展它比栈顶小，那就意味着当前栈顶的下面和栈外都比它小了，而且都是第一个比他小的东西，这时把当前栈顶弹出来可以计算以它为高的最大面积了（左边界就是弹完当前元素后的栈顶，右边界是当前栈外的元素），且做完一个之后栈顶可能还是比外面的大，还可以继续while不停做。本质上相当于当来了一个比较小的元素时，它很可能是很多位置第一个最小的右边界，有了它的位置就可以计算很多根大
#   注意因为要获取的是宽度，所以单调栈里放的是下标

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights)==0: return 0
        elif len(heights)==1: return heights[0]

        heights = [0] + heights + [0]

        stack = [0]
        maxArea = 0
        for i in range(1, len(heights)):
            while heights[i] < heights[stack[-1]]:     # 当前元素比栈顶小 -> 栈顶找到了左右第一个比它小的
                thisIdx = stack.pop(-1)
                area = heights[thisIdx] * (i-stack[-1]-1)
                if area > maxArea:
                    maxArea = area
            stack.append(i)

        return maxArea

    def otherSolution(self, heights):
        # 解法1 超时
        heights = [0] + heights + [0]
        
        maxArea = 0
        for i in range(1, len(heights)-1):
            for j in range(i-1, -1, -1):
                if heights[j] < heights[i]: break
            for k in range(i+1, len(heights)):
                if heights[k] < heights[i]: break
            
            area = heights[i] * (k-j-1)
            if area > maxArea:
                maxArea = area
        return maxArea

Solution().largestRectangleArea([2,1,5,6,2,3])
# @lc code=end

