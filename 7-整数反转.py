#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# (T86% S89%)
# 
# 整数//10可删除最后一位
# 整数%10可获取最后一位
# 
# 对整数不断循环，拿出最后一位加到反转结果中，每一轮循环反转结果*10，同时原数去掉最后一位
# 
# 需要注意的是单独处理负数，以及超出长度的判断

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        result = 0
        buf = x if x > 0 else -x

        while buf:
            result = result * 10 + buf % 10
            buf //= 10

        result = result if x > 0 else -result
        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
# @lc code=end

