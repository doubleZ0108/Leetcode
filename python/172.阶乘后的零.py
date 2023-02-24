#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
# 解法1(超时 480/500)：从1乘到n，如果累乘结尾有0则不断除10并统计，这样维护阶乘的这个数不至于太大。能通过10000，但通不过9340
#
# 解法2(T40% S35%)：纯数学，因为10只能拆分成2和5，而显然所有数中能整除5的比2更少，因此只要统计范围内所有能整除5的数字之和（这里说的能整除是可以一直除的，比如25有两个5）

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        for i in range(5, n+1, 5):
            while i%5 == 0:
                res += 1
                i //= 5
        return res

    # 解法1 超时
    def trailingZeroes(self, n: int) -> int:
        res = 0
        cnt = 1
        for i in range(1, n+1):
            cnt *= i
            while cnt % 10 == 0:
                res += 1
                cnt //= 10
        return res
# @lc code=end

