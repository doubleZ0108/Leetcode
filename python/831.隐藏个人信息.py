#
# @lc app=leetcode.cn id=831 lang=python3
#
# [831] 隐藏个人信息
#
# 解法1(T68% S97%)：没啥好说的，就是按照题意根据两张字符串的类型进行切片和拼接操作

# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        if s.count('@'):
            name, domain = s.casefold().split('@')
            return name[0].casefold() + '*'*5 + name[-1].casefold() + '@' + domain
        else:
            tel = ''
            for ch in s:
                if ch.isdigit():
                    tel += ch
            ctyNum = len(tel) - 10
            res = '***-***-' + tel[-4:]
            if ctyNum:
                res = '+' + '*'*ctyNum + '-' + res
            return res
# @lc code=end

