#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

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

