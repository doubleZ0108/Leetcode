#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#
# 解法1(T99% S59%): 贪心，明天比今天涨了，今天就买进来明天就卖出，因为就算后天还是涨，我也可以明天再买后天再卖，整体就是一个贪心的上升曲线

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        ans = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                ans += prices[i+1] - prices[i]
        return ans
# @lc code=end

