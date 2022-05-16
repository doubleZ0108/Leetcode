#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        flights_table = [[-1]*n for _ in range(n)]
        for flight in flights:
            flights_table[flight[0]][flight[1]] = flight[2]

        queue = [(src, 0, 0)]
        minPrice = -1
        while queue:
            node, turn, price = queue.pop(0)
            if turn > k: break

            for thisdst in range(n):
                thisprice = flights_table[node][thisdst] + price
                if thisdst == dst:  
                    if minPrice==-1: minPrice = thisprice
                    else: minPrice = min(minPrice, thisprice)
                else:
                    queue.append((thisdst, turn+1, thisprice))

        return minPrice

Solution().findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
# @lc code=end

