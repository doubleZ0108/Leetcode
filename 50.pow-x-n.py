#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
# 
# (正负号都单独处理)
# 解法1(内存溢出，最大递归深度exceeded): 递归，x * Pow(x, n-1)
# 
# 解法2(T78% S97%): 递归快速幂 O(log N)
#       {x^(n-1) * x, if n is odd
# x^n = {x^(n/2) * x^(n/2), if n is even
#       {1, if n is 0
# 
# 解法3(T94% S67%): 循环快速幂
#   $2^{10} = 2^{(1010)_2} = 2^{(1000)_2} \cdot 2^{(10)_2}$

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 解法3
        flag = False
        if n < 0:
            flag = True
            n = -n

        ans = 1
        while n:
            if n & 1:   # <=> n % 2 == 1
                ans *= x
            x *= x
            n >>= 1     # <=> n = n / 2

        return ans if not flag else 1 / ans


    def otherSolution(self, x, n):
        # 解法2
        flag = False
        if n<0:
            flag = True
            n = -n

        if n==0:
            return 1
        elif n % 2: # odd
            if not flag:
                return x * self.myPow(x, n-1)
            else:
                return 1 / (x * self.myPow(x, n-1))
        else:   # even
            tmp = self.myPow(x, n//2)
            if not flag:
                return tmp*tmp
            else:
                return 1 / (tmp*tmp)


        # 解法1 暴力
        if n==0:
            return 1
        elif n==1:
            return x

        if n>0:
            return x * self.myPow(x, n-1)
        else:
            return 1 / (x * self.myPow(x, -n-1))
# @lc code=end

