#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2 的幂
#
# 解法1(T37% S20%): 如果n是2的幂次方，则n对2取对数一定是整数，可再用2的成方进行还原，如果取整$log_2n$后计算$2^{log_2n}$与n不想等则n不是2的幂次方
#   注意负数和零一定不是2的幂次
#
# 解法2(T65% S39%): 不停的对n整除2，如果n始终对2取余为0，则是2的幂次方，否则不是
#   改进1(T85% S33%): 用位运算和移位运算替换取余和除法

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 解法1
        if n<=0: return False
        return pow(2, int(log(n,2))) == n


    def otherSolution(self, n):
        # 解法2
        if n <= 0: return False

        while n != 1:
            # if n%2 != 0: return False
            # n //= 2
            # 改进1
            if n & 1: return False
            n >>= 1

        return True
# @lc code=end

