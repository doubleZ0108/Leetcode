#
# @lc app=leetcode.cn id=1641 lang=python3
#
# [1641] 统计字典序元音字符串的数目
#
# 解法1(T6% S6%)：深搜，比较经典的代码实现，通过parts变量存储目前的字符串，通过idx刻画用到第几个位置了，从idx到第5个下标的元素都可以用
#     改进：因为只要求数量，这样做属实是有点浪费空间了，另外还有很多可以压缩空间的方案，比如位数不够了就只能当前几个数重复了、不通过+1的计数而是直接统计等
# - 解法2：组合数学，问题居然直接等价为$C_{n+4}^4$

# @lc code=start
class Solution:
    def countVowelStrings(self, n: int) -> int:
        res = []
        def deepin(parts, idx):
            if parts == n:
                res.append(0)
                return
            if idx >= 5:
                return
            for i in range(idx, 5):
                deepin(parts+1, i)
        
        deepin(0, 0)
        return len(res)
# @lc code=end

