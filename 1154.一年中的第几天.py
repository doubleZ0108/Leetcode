#
# @lc app=leetcode.cn id=1154 lang=python
#
# [1154] 一年中的第几天
#
"""
解法1(T5% S41%)：直接调用库函数将元旦和当前时间都转换为`Date`类型的变量，然后直接相减计算时间差
    `datetime.datetime.strptime(date, "%Y-%m-%d").date()`：将字符串变为`Date`变量

解法2(T71% S44%)：标准解法，首先把字符串分割成年月日，然后判断是否为闰年，并设立每个月有几天的数组，最后累加一下之前月的总天数再加上这个月过的天数
    闰年：(整除4 & 不能整除100) | (整除400)
"""
import datetime

# @lc code=start
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        # 解法1
        date_ = date[:4] + "-01-01"
        date1 = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(date_, "%Y-%m-%d").date()
        return (date1-date2).days + 1

    def otherSolution(self, date):
        # 解法2
        def isLeap(year):
            return (year%4==0 and year%100!=0) or (year % 400 == 0)

        year, month, day = tuple(map(lambda x: int(x), date.split('-')))
        days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if isLeap(year):
            days_of_month[2-1] += 1
        
        res = 0
        for i in range(month-1):
            res += days_of_month[i]
        return res + day 
# @lc code=end

