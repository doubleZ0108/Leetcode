#
# @lc app=leetcode.cn id=389 lang=python
#
# [389] 找不同
#
# 解法1(T70% S42%)：题目没说清楚，每个字符可能出现多次，因此要用字典不能只用集合。先一次遍历s构建字典，然后一次遍历t，如果某个字符不在字典中或个数已经减为0了就返回

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        table = {}
        for l in s:
            table[l] = table.get(l, 0) + 1

        for l in t:
            if l not in table or table[l] == 0: return l
            else: table[l] -= 1
# @lc code=end

