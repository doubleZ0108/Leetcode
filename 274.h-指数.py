#
# @lc app=leetcode.cn id=274 lang=python
#
# [274] H 指数
#
# 首先要想清楚H指数不一定是citations里的数
# 
# 解法1(T9% S47%): 先排序，从发表的总篇数开始，h指数不会大于发的论文篇数n，每次从头找第一个引用量大于h的，如果这个位置满足后面的文章数等于h，则这个位置就是最大的h
# 
# 解法2(T57% S91%): 一次遍历的方法一上来就先想到了，只是一直有点小毛病现在捋一下。首先从大到小排序，从头遍历，找到第一个引用量比标号少的（注意从1开始数文章数）；有一种要单独判断，如果最小的引用数都比文章数大，那这人是大牛，h指数就是发的文章数

# @lc code=start
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        n = len(citations)
        for i in range(n):
            if citations[i] < i+1:
                return i

        if citations[-1] >= n:
            return n
        return 0


    def otherSolution(self, citations):
        citations.sort()
        n = len(citations)
        for h in range(n, -1, -1):
            for i in range(n):
                if citations[i]>=h:
                    if n-i == h:
                        return h
        return 0
# @lc code=end

