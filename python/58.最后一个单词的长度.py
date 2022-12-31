#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#
# 解法1(T98% S35%)：python的语法一行就可以搞定 rstrip()去除右侧的空格，split()以空格划分字符串，取最后一个数组元素就是最后一个单词

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split(" ")[-1])
# @lc code=end

