#
# @lc app=leetcode.cn id=258 lang=python
#
# [258] 各位相加
#
# 解法1(T42% S57%): 基础做法，两重循环，外层不断循环直至唯一为主，里层不断循环%/逐位相加
#
# 解法2(T97% S76%): 要求$O(1)$解完，观察到比如一个三位数num(abc) = 100a+10b+c，而我们要求的是a+b+c，将num稍微变形num = 99a+9b+(a+b+c)，因此只要num对9取余，剩下的部分就是a+b+c。当然还要特别判断下如果一个大于10的数正好是9的倍数，最终应该返回的是9

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 解法2
        if num < 10: return num
        return num % 9 if num%9!=0 else 9

    def otherSolution(self, num):
        # 解法1
        while num >= 10:
            tmp = num
            num = 0
            while tmp:
                num += tmp % 10
                tmp //= 10
        return num
# @lc code=end

