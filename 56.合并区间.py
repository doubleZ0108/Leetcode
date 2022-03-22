#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#
# 解法1(T76% S64%): 先按照左端点排序，然后一次遍历进行合并，用一个结果栈，栈顶始终是等待跟下个合并的状态，如果当前的左端点比栈顶右端点小则二者可以合并，注意合并时左端点不一定谁小、右端点不一定谁大，直接通过min和max选取即可

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][-1]:
                ans[-1] = [min(intervals[i][0], ans[-1][0]), max(intervals[i][1], ans[-1][1])]
            else:
                ans.append(intervals[i])
        return ans
# @lc code=end

