#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#
# 解法1(T90% S65%)：还是按照题意一步一步写就好，首先通过lstrip()去除前面的空格，然后判断下数字的正负号，依次遍历字符串直到遇到非数字，把所有数字字符都保存到一个数组中，如果数组为空则直接返回0，否则将数组拼接字符串并转为整数，最后再根据int范围截断一下

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if len(s) > 0:
            if s[0] in ['+', '-']:
                flag = s[0]
                s = s[1:]
            else: flag = '+'

        res = []
        for c in s:
            if c.isnumeric(): res.append(c)
            else: break

        if len(res) == 0: return 0

        num = int("".join(res))
        if flag == '+':
            if num > 2**31-1: return 2**31-1
        else:
            num = -num
            if num < -2**31: return -2**31
        return num
# @lc code=end

