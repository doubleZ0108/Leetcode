#
# @lc app=leetcode.cn id=682 lang=python
#
# [682] 棒球比赛
#
# 解法1(T87% S41%)：是一道很简单的题，按照题干写就好了，类似用一个栈来维护分数。最后输出数组求和结果有个小技巧可以用reduce()，但如果数组里只有一个数时lambda的两个引用就会报错，因此可以在最后往结果数组里补两个0

# @lc code=start
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []
        for op in ops:
            if op == "C":
                points.pop()
            elif op == "D":
                points.append(points[-1]*2)
            elif op == "+":
                points.append(points[-2]+points[-1])
            else:
                points.append(int(op))
        points.append(0)
        points.append(0)
        return reduce(lambda x,y: x+y, points)
# @lc code=end

