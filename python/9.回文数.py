#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#
# 解法1(T62% S98%): 按照题意如果是负数直接False，如果是个位数直接True，否则通过while % //将数字反转比较
# 
# 解法2(T8% S93%): 转为字符串判断
#   题干说了不推荐这么做

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x<10:
            return True
        
        rev, save = 0, x
        while x:
            rev = rev*10 + x%10
            x //= 10
        return rev == save

    def otherSolution(self, x):
        if x<0:
            return False

        return str(x)[::-1] == str(x)
# @lc code=end

