#
# @lc app=leetcode.cn id=2383 lang=python
#
# [2469] 温度转换
#
# 解法1(T97% S96%)：可能是可怜我，出了道直接送分的题

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32.]
# @lc code=start
# @lc code=end