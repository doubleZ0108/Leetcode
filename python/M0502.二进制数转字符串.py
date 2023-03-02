#
# @lc app=leetcode.cn id=M0502 lang=python
#
# [面试题 05.02] 二进制数转字符串
#
# 解法1(T87% S57%)：只要知道小数的二进制转换方式即可，对0~1的小数部分乘2取整正着写，比如0.625这个例子，再就是如果当前位数已经超过32-2位就可以提前终止了

# @lc code=start
class Solution:
    def printBin(self, num: float) -> str:
        res = ""
        while num != 0:
            num *= 2
            if num >= 1.0:
                res = res + "1"
                num -= 1.0
            else:
                res = res + "0"
            
            if len(res) + 2 > 32:
                return "ERROR"
        return "0." + res
# @lc code=end