#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 统计各位数字都不同的数字个数
#
# 解法1(T100% S32%)：高中还是初中的排列组合数学题，而且是最经典的查数字，记得高中做这种题的精髓在于数字的第一位不能为0，所以第一位只有9种可能。具体来说，我们从1位数开始累加，直到加到n位数，比如对于4位数|_a_|_b_|_c_|_d_|，各位都不同的数字有多少呢？a有9种可能（因为第一位不能为0），b也有9种可能（不能跟a一样但是多了一个0可选），c有8种可能（不能跟a和b一样），d依次类推有7种可能。
#     知道了数学上的原理剩下的就是写代码的事了，这里用了两个Python的小技巧：`range()`可以用于直接生成等差数列，`reduce()`可以实现列表内元素相乘

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0: return 1

        res = 10
        for i in range(2, n+1):
            res += reduce(lambda a, b: a*b, range(9, 10-i, -1)) * 9
        return res
# @lc code=end

