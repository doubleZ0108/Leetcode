#
# @lc app=leetcode.cn id=1237 lang=python3
#
# [1237] 找出给定方程的正整数解
#
# 解法1(T32% S67%)：说实话没太明白这道题想干什么，因为题设规模很小，直接两重遍历x和y，调用接口的f函数判断是否等于z值，测试了全部的9个最大规模样例都没问题，就结束了
#     改进1：既然提到了单调递增函数，肯定是想利用二分查找，但是二维数组的二分查找可跟一维不一样，比如当前结果大了，那究竟是x影响的还是y是不得而知的，因为无法预估函数形式，所以意义不大

# @lc code=start
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        for x in range(1, 1001):
            for y in range(1, 1001):
                cal = customfunction.f(x, y)
                if cal == z:
                    res.append([x, y])
                elif cal > z:
                    break
        return res
        
# @lc code=end

