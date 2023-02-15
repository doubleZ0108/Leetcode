#
# @lc app=leetcode.cn id=1250 lang=python3
#
# [1250] 检查「好数组」
#
# 解法1(T100% S80%)：完全是个数论问题，本题的数学原理简单来说就是如果原数组的最小公约数为1，则可以实现ax+by…=1，否则不行

# @lc code=start
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1
# @lc code=end

