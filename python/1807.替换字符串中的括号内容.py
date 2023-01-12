#
# @lc app=leetcode.cn id=1807 lang=python3
#
# [1807] 替换字符串中的括号内容
#
# 题目还是非常有趣的，类似于实现编程语言的print格式化功能。

# 解法1(T45% S68%): 首先将knowledge转为哈希表加速查询，由于key不会重复所以非常简单；然后一次遍历字符串s，如果发现左括号则不断试探直到找到右括号，将中间的字符串作为token在哈希表中查找对应的结果，否则直接加入新字符串中

# @lc code=start
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_table = {}
        for key, val in knowledge:
            knowledge_table[key] = val

        res = ""
        i = 0
        while i<len(s):
            if s[i] == '(':
                token = ""
                while s[i]!=')':
                    i += 1
                    token += s[i]
                i += 1
                if token[:-1] not in knowledge_table:
                    res += '?'
                else :
                    res += knowledge_table[token[:-1]]
            else:
                res += s[i]
                i += 1
        return res
# @lc code=end

