#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#
# 解法1(T13% S68%)：暴力循环，如果乘方等于num则为True，如果比num大了则返回False
#
# 解法2(T5% S5%)：把所有完全平方数算出来存起来，最后直接判断num是否在这个列表中
# 
# 解法3(T99% S80%)：二分查找，如果中值的平方是就找到了，如果到最后还没有那就是不是

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 解法3
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid*mid == num: return True
            elif mid*mid > num: right = mid - 1
            else: left = mid + 1
        return False

    def otherSolution(self, num):
        # 解法1
        if num==1: return True
        for i in range(1, num//2+2):
            if i*i == num: return True
            elif i*i > num: return False

        # 解法2
        sqres = []
        i = 1
        while i*i<2**31-1:
            sqres.append(i*i)
            i += 1

        return num in sqres
# @lc code=end

