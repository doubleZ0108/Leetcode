#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#
# 解法1(T80% S65%)：题目反过来就简单多了，只需要每位乘以对应26的位次幂就好，注意是从1开始计数而不是0就好

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for idx, ch in enumerate(columnTitle[::-1]):
            res += (ord(ch) - ord('A') + 1) * 26**idx
        return res
# @lc code=end

