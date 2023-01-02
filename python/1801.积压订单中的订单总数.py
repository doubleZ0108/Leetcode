#
# @lc app=leetcode.cn id=1801 lang=python3
#
# [1801] 积压订单中的订单总数
#

# @lc code=start
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_storage = []
        sell_storage = []

        for order in orders:
            price, amount, orderType = order

            if orderType == 0:
                while amount:
                    # 如果这里调用一遍nsmallest会超时，heapq的数组可以直接通过0元素访问最小值
                    # sell_price, sell_amount = heapq.nsmallest(1, sell_storage, key=lambda x: x[0])[0]
                    if not sell_storage or sell_storage[0][0] > price:
                        heapq.heappush(buy_storage, [-price, amount])
                        break

                    sell_price, sell_amount = heapq.heappop(sell_storage)
                    if sell_amount > amount:
                        heapq.heappush(sell_storage, [sell_price, sell_amount-amount])
                        break
                    elif sell_amount < amount:
                        amount -= sell_amount
                    else:
                        break
            else:
                while amount:
                    if not buy_storage or -buy_storage[0][0] < price:
                        heapq.heappush(sell_storage, [price, amount])
                        break

                    buy_price, buy_amount = heapq.heappop(buy_storage)
                    if buy_amount > amount:
                        heapq.heappush(buy_storage, [buy_price, buy_amount-amount])
                        break
                    elif buy_amount < amount:
                        amount -= buy_amount
                    else:
                        break
        
        return (sum(map(lambda x: x[1], buy_storage)) + sum(map(lambda x: x[1], sell_storage))) % (10**9 + 7)


Solution().getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]])
# @lc code=end

