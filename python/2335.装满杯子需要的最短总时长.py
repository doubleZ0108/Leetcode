#
# @lc app=leetcode.cn id=1154 lang=python
#
# [2335] 装满杯子需要的最短总时长
#
# 解法1(T70% S53%)：通过几个小例子可以发现，每次只需要接当前剩余最多的两个杯子各一杯，如果没有两杯剩余则再接一杯即可，因此不断循环，循环内部排序，判断最大的两个元素即可

# @lc code=start
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        while sum(amount) > 0:
            amount.sort()
            res += 1
            if amount[-1]>0 and amount[-2]>0:
                amount[-1] -= 1
                amount[-2] -= 1
            else:
                amount[-1] -= 1
        return res
# @lc code=end