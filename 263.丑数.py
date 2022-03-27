#
# @lc app=leetcode.cn id=263 lang=python
#
# [263] 丑数
#
# 解法1(T96% S50%): 这个数不停除2，除干净之后再不停除3，再不停除5，如果最后没了(剩1)就证明是丑数
#   注意正整数的条件

# @lc code=start
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        elif n < 7:
            return True

        for item in [2, 3, 5]:
            while n % item == 0:
                n //= item

        if n == 1:
            return True
        return False
# @lc code=end

