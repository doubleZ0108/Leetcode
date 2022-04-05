#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#
# 解法1(T93% S100%): 主要要解决空间复杂度的问题，用一个目标行长度的队列来维护，每次取出首元素跟上次的数字相加塞到队尾，对于第i行循环i次即可，最后再多插入队尾一个1

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        for i in range(rowIndex):
            last = 0
            for j in range(i+1):
                first = ans.pop(0)
                ans.append(first + last)
                last = first
            ans.append(1)
        return ans
# @lc code=end

