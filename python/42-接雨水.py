#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) in [0, 1]:
            return 0

        '''
            向右寻找第一个比我高的，计算这中间的水量后，把我移动到最高处继续迭代
            【右边比我矮的也可能存水（e.g. 4，2，3）】
        '''
        # total = 0
        # i = 0
        # while i < len(height):
        #     for j in range(i+1, len(height)):
        #         if height[j] >= height[i]:
        #             k = i + 1
        #             while k < j:
        #                 total += min(height[i], height[j]) - height[k]
        #                 k += 1
        #             i = j
        #             break
        #     if j == len(height) - 1:
        #         i += 1
        # return total

        '''
            对于每一个水坑 找左边最高的和右边最高的，它们的（min - 当前高度）就是这个坑能接受的水
            【大数据超时】
        '''
        total = 0
        for i in range(len(height)):
            max_left_index, max_right_index = i - 1, i + 1
            max_left, max_right = 0, 0
            while max_left_index > -1:
                if height[max_left_index] > max_left:
                    max_left = height[max_left_index]
                max_left_index -= 1

            while max_right_index < len(height):
                if height[max_right_index] > max_right:
                    max_right = height[max_right_index]
                max_right_index += 1

            diff = min(max_left, max_right) - height[i]
            if diff > 0:
                total += diff

        return total

# @lc code=end

