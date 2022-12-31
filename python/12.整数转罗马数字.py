#
# @lc app=leetcode.cn id=12 lang=python
#
# [12] 整数转罗马数字
#
# 解法1(T88% S48%)：没什么技巧的纯流程题，按照题干依次判断，首先先while减去足量的1000，然后判断剩余是否大于900/大于500/大于400，最后再while减去足量的100；然后再判断剩余是否大于90/50/40，然后再while减去足量的10；最后再判断剩余是否大于9/5/4，最终再减去足量的1直到num==0

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        while num >= 1000:
            roman += 'M'
            num -= 1000
        if num >= 900:
            roman += 'CM'
            num -= 900
        elif num >= 500:
            roman += 'D'
            num -= 500
        elif num >= 400:
            roman += 'CD'
            num -= 400
        while num >= 100:
            roman += 'C'
            num -= 100
        
        if num >= 90:
            roman += 'XC'
            num -= 90
        elif num >= 50:
            roman += 'L'
            num -= 50
        elif num >= 40:
            roman += 'XL'
            num -= 40
        while num >= 10:
            roman += 'X'
            num -= 10
        
        if num >= 9:
            roman += 'IX'
            num -= 9
        elif num >= 5:
            roman += 'V'
            num -= 5
        elif num >= 4:
            roman += 'IV'
            num -= 4
        while num:
            roman += 'I'
            num -= 1
        
        return roman
# @lc code=end

