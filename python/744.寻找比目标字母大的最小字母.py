#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#
# 解法1(T33% S81%)：按照题干描述一次查找，如果在范围内找到第一个比target字母大的则返回这位，如果循环下标还停在0或者数组结尾则返回首位字符
#     python中字符大小比较要通过`ord()`实现

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        while i<len(letters) and ord(letters[i])<=ord(target):
            i += 1
        if i==0 or i==len(letters):
            return letters[0]
        else:
            return letters[i]
# @lc code=end

