#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#
# 解法1(T24% S33%)：两个矩形重叠可能会有很多很多情况，如果写很多判定很容易遗漏，但两矩形不重叠只有四种可能，橙色矩形完全在蓝色矩形上/右/下/左时肯定不重叠

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a1, b1, a2, b2 = rec1
        c1, d1, c2, d2 = rec2
        return not (d1>=b2 or c1>=a2 or d2<=b1 or c2<=a1)
# @lc code=end

