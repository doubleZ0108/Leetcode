#
# @lc app=leetcode.cn id=2319 lang=python
#
# [2427] 公因子的数目
#
# 解法1(T72% S28%)：没啥好说的，从1循环到二者最小值，如果能被同时整除则计数器加一

# @lc code=start
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        for i in range(1, min(a, b)+1):
            if a % i == 0 and b % i == 0:
                res += 1
        return res
# @lc code=end