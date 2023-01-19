#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#
# 解法1(T96% S29%)：直接使用语言自带的API，注意python讲字符串直接变为小写的是`.lower()`，toLowerCase()不是这么用的

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
# @lc code=end

