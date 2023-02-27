#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#
# 解法1(T89% S55%)：现有高度排序后就得到了期待的数组，一次同时遍历，二者不相同的位置计数器加一即可

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expecteds = sorted(heights)
        res = 0
        for height, expect in zip(heights, expecteds):
            if height != expect:
                res += 1
        return res

# @lc code=end

