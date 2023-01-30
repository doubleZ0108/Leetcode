#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
# 解法1(T69% S97%)：直接双指针交换元素，不知道要考什么这道题

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i<j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
# @lc code=end

