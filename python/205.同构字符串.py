#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
 #解法1(错误)：直接用哈希表统计两个字符中字母出现的次数，如果排序后的次数数组相等则返回True，但如下例子会出错❌
    # "bbbaaba"
    # "aaabbba"
    
# 解法2(T96% S18%)：因为两字符串长度肯定相等，那么同步遍历两字符串，并维护哈希表，如果s的当前字符不在哈希表中则将对应关系加入哈希表，否则如果当前对应与哈希表中存的不一样则False；做完一遍之后还需要交换s和t字符串再做一遍，否则会遇到这种情况⬇️
    # "badc"
    # "baba"

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        stored = set()
        for chs, cht in zip(s, t):
            if chs not in table:
                table[chs] = cht
            else:
                if table[chs] != cht:
                    return False

        s, t = t, s
        table = {}
        stored = set()
        for chs, cht in zip(s, t):
            if chs not in table:
                table[chs] = cht
            else:
                if table[chs] != cht:
                    return False

        return True
# @lc code=end

