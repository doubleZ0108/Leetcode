#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#
# 解法1(T93% S86%): 不用像数组加法一样储存进位什么的，从末尾开始逐位+1，如果+1完发现没超过10就可以直接返回结果了；+1完发现=10则有进位，如果当前不是数组头则重复循环即可；如果当前已经是数组头，则返回多一位的数组即可【提前终止】

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    return [1]+digits
# @lc code=end

