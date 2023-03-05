#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#
# 解法1(T51% S93%)：非常经典的问题，跟爬楼梯是一样的通项公式，包括递归法、一维数组动态规划法、直接数学公式法，和这个双变量轮转的最优动态规划法

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b
# @lc code=end

