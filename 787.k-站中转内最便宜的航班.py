#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#
# 解法1(超时)：图的广搜。外层通过queue广搜，弹出一个节点遍历图中所有起始点为此弹出node的边，如果这条边的dst就是终点则添加到可能结果中（实现时只保存最小的价格就好），如果不是终点就把dst作为新的src入队，并让其搜索层次+1，如果发现某次出对已经是k次中转之外的就可以提前返回了
#   改进1(超时)：猜想应该是重复查找耗时，因此首先将图表示为邻接矩阵，这样每次遍历只需遍历一行
#   改进2(会出错)：把遍历过的（src，dst）对存在visited防止重复遍历，但从不同的路径遍历来很可能价钱不一样的，这样会无法得到最优解
#   改进3(超时): 把邻接矩阵换成邻接表，还是会有太多没意义的中转入队
#   改进4(超时): 也像递归方法一样加入memo，能通过刚刚超时的例子了，但更大的还是会超时
#
# 解法2(T5% S54%)：还是广搜，只是用递归实现，这样可以加入memo。memo的设计很巧妙，并不是存储某个src到某个dst的过往值，而是存某个src到最终目标的当前最小价格。递归终止条件为：轮次用完了 or 走到目标了 or memo在这个起点和轮次恰好能走到最终目标，如果没终止则依次遍历航班信息bfs搜索当前价格并刷新最小价格，最后将最小价格存下来并返回

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        INF = 1e06+1
        memo = [[-1]*(k+1) for _ in range(n)]

        def bfs(thisstr, turn):
            if turn < -1: return INF
            if thisstr == dst: return 0
            if memo[thisstr][turn]!=-1: return memo[thisstr][turn]

            minPrice = INF
            for flight in flights:
                if flight[0] == thisstr:
                    thisprice = bfs(flight[1], turn-1)+flight[2]
                    minPrice = min(minPrice, thisprice)

            memo[thisstr][turn] = minPrice
            return minPrice

        res = bfs(src, k)
        return res if res<INF else -1


    def otherSolution(self, n, flights, src, dst, k):
        INF = 1e06+1

        queue = [(src, 0, 0)]   # 当前扩展到的节点，到目前为止的轮次，到目前为止的总价格
        minPrice = INF
        memo = [[-1]*(k+1) for _ in range(n)]

        while queue:
            node, turn, price = queue.pop(0)
            if turn > k: break

            if memo[node][k-turn] != -1:
                minPrice = min(minPrice, memo[node][k-turn]+price)
                continue

            for flight in flights:
                if flight[0] == node:
                    thisdst, thisprice = flight[1], flight[2]
                    if thisdst == dst:  
                        thisprice += price
                        minPrice = min(minPrice, thisprice)
                        memo[node][turn] = thisprice
                    else:
                        if memo[thisdst][k-turn-1] != -1:
                            minPrice = min(minPrice, memo[thisdst][k-turn-1])
                        else:
                            queue.append((thisdst, turn+1, thisprice+price))


        return minPrice if minPrice != INF else -1

# @lc code=end

