#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根 
#
# 解法1(爆内存): 依次循环直到 i^2 < target < (i+1)^2
#   改进(T57% S83%)：可以从1～x/2二分查找降复杂度
# 
# 解法2(T80% S98%): 牛顿迭代法

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:   # 0, 1
            return x

        # 解法2
        t = x
        while t > x//t:
            t = (t**2 + x) // (2*t)
        return t
    
    def otherSolution(self, x):
        if x < 2:
            return x

        # 解法1: 直接顺序解会爆内存
        for i in range(1, x//2+1):
            if i*i <= x and (i+1)*(i+1) > x:
                return i

        # 解法1 改进
        i, j = 1, x//2+1
        while i<=j:
            mid = (i+j)//2
            if mid**2 <= x:
                i = mid + 1
            else:
                j = mid - 1
        return (i+j)//2
# @lc code=end