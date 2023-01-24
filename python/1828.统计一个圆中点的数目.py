#
# @lc app=leetcode.cn id=1828 lang=python3
#
# [1828] 统计一个圆中点的数目
#
# 解法1(T56% S87%)：不知道为什么是中等的题，只需要知道如何判断二维坐标下一个点(x,y)是否在圆(a,b,r)内，只需满足 $\sqrt{(x-a)^2+(y-b)^2} \le r$ 即可

# @lc code=start
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for query in queries:
            cnt = 0
            for point in points:
                if pow((query[0]-point[0])**2 + (query[1]-point[1])**2, 0.5) <= query[2]:
                    cnt += 1
            res.append(cnt)
        return res
# @lc code=end

