#
# @lc app=leetcode.cn id=1637 lang=python3
#
# [1637] 两点之间不包含任何点的最宽垂直面积
#
# 解法1(T70% S29%)：不懂这道题咋出的，直接对x坐标排序，然后一次遍历，计算相邻的两点x方向的差，这一定是中间不包含任何点的宽度，选最大的即可

# @lc code=start
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        res = 0
        for i in range(1, len(points)):
            res = max(res, points[i][0]-points[i-1][0])
        return res
# @lc code=end

