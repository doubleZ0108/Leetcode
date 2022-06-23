#
# @lc app=leetcode.cn id=415 lang=python
#
# [415] 字符串相加
#
# 解法1(T60% S99%)：非常标准的一道题，首先不妨把字符串都翻转[::-1]下方便计算，然后逐位相加获取余数加入结果中并且保留除数作为进位，二者公共的部分做完之后再加一下更长的字符串，最后如果还有进位要再添加一位，再把结果翻转下即可

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        res = ""
        i = 0
        remain = 0
        while i<len(num1) and i<len(num2):
            buf = int(num1[i]) + int(num2[i]) + remain
            res += str(buf % 10)
            remain = buf // 10
            i += 1
        while i<len(num1):
            buf = int(num1[i]) + remain
            res += str(buf % 10)
            remain = buf // 10
            i += 1
        while i<len(num2):
            buf = int(num2[i]) + remain
            res += str(buf % 10)
            remain = buf // 10
            i += 1
        if remain:
            res += str(remain)
        return res[::-1]
# @lc code=end

