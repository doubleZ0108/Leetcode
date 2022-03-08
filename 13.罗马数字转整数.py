#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#
# 解法1(T15% S87%): 首先建立每个字符的整数权重字典，逐位扫描，先看如果能跟后一个数特殊匹配，则减去当前数继续循环，否则普普通通加上该数
#   改进(T72% S98%)：将特殊的6个配对也加入字典中，用字符串切片看跟后一个数的组合在不在字典中，如果在直接跳过两位

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 改进
        score_table = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }

        i, result = 0, 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in score_table:
                result += score_table[s[i:i+2]]
                i += 2
            else:
                result += score_table[s[i]]
                i += 1
        
        return result

    def otherSolution(self, s):
        # 解法1
        score_table = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        }

        result = 0
        for i in range(len(s)):
            if i+1 < len(s):   # i+1 is valid
                if (s[i]=='I' and s[i+1] in ['V', 'X']) or \
                   (s[i]=='X' and s[i+1] in ['L', 'C']) or \
                   (s[i]=='C' and s[i+1] in ['D', 'M']):
                    result -= score_table[s[i]]
                    continue
            result += score_table[s[i]]
        
        return result
# @lc code=end

