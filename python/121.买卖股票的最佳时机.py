#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#
# 解法1(超时)：一次循环，每次计算后面序列中最大值和当前值的差，整体选最大的一种情况
#   改进1(超时)：首先先把数组最大最小值的差求出来，如果某次收益跟这个相等就可以直接返回了
#   改进2(超时): 首先判断数组是否倒序有序，直接返回0
#   改进3(T5% S15%): 首先一次逆序遍历，把结尾所有的0排除
#       后面的大样例好几个都是前面没多少有效数，后面有几千个0
#
# 解法2(T94% S48%): 一次遍历，记录遇到过的最小价格和当前最大收益，不断更新这两个数
#   代码“优化”(T56% S30%): 直接用min和max库函数没有if判断快

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i]-min_price > max_profit:
                max_profit = prices[i]-min_price
            if prices[i] < min_price:
                min_price = prices[i]

            # 代码“优化” 用min和max没有直接if快
            # max_profit = max(max_profit, prices[i]-min_price)
            # min_price = min(min_price, prices[i])
        return max_profit


    def otherSolution(self, prices):
        if len(prices) < 2:
            return 0

        # 改进3
        for i in range(len(prices)-1, -1, -1):
            if prices[i]!=0:
                break
        prices = prices[:i+1]
        
        # 改进2
        if all([prices[i+1]<=prices[i] for i in range(len(prices)-1)]):
            return 0
        
        profit_max = max(prices) - min(prices)

        ans = 0
        for i in range(len(prices)-1):
            this = max(prices[i+1:]) - prices[i]
            if this > ans:
                ans = this
                # 改进1
                if ans == profit_max:
                    return ans
        return ans
# @lc code=end

