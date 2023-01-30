#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# 解法1(T12% S91%)：根205题几乎一样，首先把s转换为数组并判断长度是否二者匹配，分别将pattern和strs作为哈希表的key和val来判断是否有重复的键值对应关系

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split(" ")
        if len(pattern) != len(strs): return False

        table = {}
        for pat, st in zip(pattern, strs):
            if pat not in table:
                table[pat] = st
            elif table[pat] != st:
                return False

        table = {}
        for pat, st in zip(strs, pattern):
            if pat not in table:
                table[pat] = st
            elif table[pat] != st:
                return False

        return True
# @lc code=end

