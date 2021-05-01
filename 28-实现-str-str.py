#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

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

