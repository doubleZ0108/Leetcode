#
# @lc app=leetcode.cn id=292 lang=python
#
# [292] Nim 游戏
#
# 解法1(T97% S73%)：这题感觉是个逻辑题，试了1～16的所有答案发现只要是4的倍数就会输，其他都有机会赢。如果石头总数为4的倍数，那么不管这轮我拿多少块，对手总可以让我下一局依然是4的倍数，从而让我输掉比赛。

# @lc code=start
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
# @lc code=end

