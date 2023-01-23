#
# @lc app=leetcode.cn id=2303 lang=python3
#
# [2303] 计算应缴税款总额
#
# 解法1(T63% S15%)：题看起来挺简单，但逻辑循环还是有一点点绕，以例一为例，初始的3元按50%缴税，接下来的(7-3)按10%缴税，最后7~12阶段只剩下3按25%缴税，因此循环之际肯定是要同时访问i和i-1，因此不妨先给brackets数组左边加上一个空置防止数组越界写起来麻烦，很自然的想到增加[0, 0]代表0元的时候税为0，接下来从i=1开始循环，当前要缴税的金额就是 符合这一档的收入 和 这一档区间的最小值，再乘以税率就是这一档应缴的税，同时让income直接减去去见长度并作为循环终止的依据，如果income减为负了，就代表我根本没那么多钱，后面的设档压根没用上

# @lc code=start
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        brackets = [[0, 0]] + brackets
        res = 0
        i = 1
        while i<len(brackets) and income>0:
            res += min(brackets[i][0]-brackets[i-1][0], income) * brackets[i][1] * 0.01
            income -= (brackets[i][0]-brackets[i-1][0])
            i += 1
        return res
# @lc code=end

