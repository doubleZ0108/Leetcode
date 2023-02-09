#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#
# 解法1(T72% S49%)：外层一重循环，内层从下标开始切片长度为搜索串的长度判断二者是否相等

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for i in range(len(haystack)):
            if i + len(needle) <= len(haystack):
                if haystack[i:i+len(needle)] == needle:
                    return i
        
        return -1

# @lc code=end

