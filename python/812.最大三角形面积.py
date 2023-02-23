#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#
# 解法1(T48% S62%)：看数据规模完全就是让你来三重循环暴力求解的，那现在问题就变成了给定平面内任意三点$(x_1,y_1) \ (x_2,y_2) \ (x_3, y_3)$，如何求解它们围成三角形的面积 = 1/2 * |(y3-y2)x1+(x2-x3)y1+(x3y2-x2y3)|

# @lc code=start
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in range(0, len(points)-2):
            for j in range(i+1, len(points)-1):
                for k in range(j+1, len(points)):
                    res = max(res, 0.5*abs((points[k][1]-points[j][1])*points[i][0] + (points[j][0]-points[k][0])*points[i][1] + (points[k][0]*points[j][1] - points[j][0]*points[k][1])))
        return res
# @lc code=end

