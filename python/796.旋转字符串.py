#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#
# 解法1(T89% S92%)：没啥好说的，如果长度都不相等肯定不同，依次旋转一位s看是否能等于goal，最多循环字符长度就够了

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        for _ in range(len(s)):
            if s == goal: return True
            s = s[1:] + s[0]
        return False

# @lc code=end

