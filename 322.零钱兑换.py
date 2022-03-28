#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return -1
        if amount <= 0:
            return 0

        dp = [-1 for _ in range(amount+1)]
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(1, amount+1):
            if dp[i] == 1:
                continue
            min_count = float('inf')
            for coin in coins:
                if coin < i:
                    this_count = 1 + dp[i-coin]
                    min_count = min(min_count, this_count)
            dp[i] = min_count

        return -1 if dp[-1]==float('inf') else dp[-1]

    
    # 一直超时 不保证正确
    def otherSolution(self, coins, amount):
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return -1

        # 解法1
        # 改进1
        min_table = [-1 for _ in range(amount)]
        def coinCount(coins, amount):
            if not coins:
                return -1
            if amount <= 0:
                return 0
            if amount in coins:
                return 1
            if min_table[amount-1] != -1:
                return min_table[amount-1]

            min_coin_change = -1
            for coin in coins:
                if coin == amount:
                    min_coin_change = 1
                    break
                elif coin > amount:
                    continue
                else:
                    this_change = coinCount([c for c in coins if c<=amount-coin], amount-coin)
                    if this_change >= 1:
                        if min_coin_change == -1:
                            min_coin_change = 1 + this_change
                        else:
                            min_coin_change = min(min_coin_change, this_change+1)

                        if min_table[amount-1] == -1:
                            min_table[amount-1] = 1+this_change
                        else:
                            min_table[amount-1] = min(min_table[amount-1], this_change+1)
            return min_coin_change

        return coinCount(coins, amount)

if __name__ == "__main__":
    print(Solution().coinChange([1,2,5], 11))
# @lc code=end

