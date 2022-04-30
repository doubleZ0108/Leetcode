#
# @lc app=leetcode.cn id=374 lang=python
#
# [374] 猜数字大小
#
# 解法1(T97% S83%)：最经典基础的编程题，整体思想是二分查找，每次猜中间数对不对，不对就进行二分折半

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while True:
            med = (left+right)//2
            flag = guess(med)
            if not flag: return med
            elif flag == -1: right = med - 1
            else: left = med + 1

        return med
        
# @lc code=end

