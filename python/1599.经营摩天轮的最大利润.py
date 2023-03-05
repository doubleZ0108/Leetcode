#
# @lc app=leetcode.cn id=1599 lang=python3
#
# [1599] 经营摩天轮的最大利润
#
# 这道题整体很迷，看示例不难理解但代码写起来不知道为什么就是有问题，非得按照题解这种先把每个人都遍历一遍
#
# 解法1(无法AC)：就按照题干说的，每次最多上4个人，如果当前排队的人超过4个那直接让他们上，否则新来一批人并判断上几个，摩天轮每轮都必须转一下，所有游玩人数加上这次放进来的即可，再计算个最大最大利润，不知道问题出在哪，看了好几遍也没找到代码里的问题
#
# 解法2(T11% S9%)：还必须得先依次遍历每组人，把每组+remain这种情况先遍历完再依次循环remain直到为空，其间计算每一次循环时的利润并更新最大利润

# @lc code=start
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxProf, minTurn = 0, 0
        i, remain = 0, 0
        players, rottime = 0, 0
        for customer in customers:
            thisturn = customer + remain
            players += min(thisturn, 4)
            remain = thisturn - min(thisturn, 4)
            rottime += 1
            prof = players*boardingCost - rottime*runningCost
            if prof > maxProf:
                maxProf = prof
                minTurn = rottime
        while remain:
            players += min(remain, 4)
            remain -= min(remain, 4)
            rottime += 1
            prof = players*boardingCost - rottime*runningCost
            if prof > maxProf:
                maxProf = prof
                minTurn = rottime
        
        return minTurn if maxProf>0 else -1
        
# @lc code=end

