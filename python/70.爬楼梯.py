#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#
# 解法1: 递归 F(N) = F(N-1) + F(N-2)
# 
# 解法2(T30% S96%): DP解法，变为for循环，用一个数组来储存之前的状态
#   改进(T64% S80%)：不需要数组，只循环最后的两个变量
# 
# 解法3(T90 S99%): 数学方法斐波那契数列，递推式 → 通项公式 （注意通项公式是从0开始）

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n

        # 解法3 通项公式
        # 注意通项公式从0开始
        return int((1/(5**0.5)) * (((1+5**0.5)/2)**(n+1) - ((1-5**0.5)/2)**(n+1)))
    
    def otherSolution(self, n):
        if n < 3:
            return n
        
        # 解法1 递归
        return self.climbStairs(n-1) + self.climbStairs(n-2)

        # 解法2 数组
        F = [0, 1, 2]
        for i in range(3, n+1):
            F.append(F[-2] + F[-1])
        return F[-1]

        # 解法2 改进 
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b

# @lc code=end

