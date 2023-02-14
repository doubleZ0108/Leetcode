#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#
# 解法1(T89% S16%)：按照题干描述一次循环字符串即可，A设置一个计数器，L判断i-1, i, i+1三者是否下标合理并且都为L

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        abscnt = 0
        for i in range(len(s)):
            if s[i] == 'A':
                abscnt += 1
                if abscnt >= 2:
                    return False
            elif s[i] == 'L':
                if i-1>=0 and i+1<len(s):
                    if s[i-1] == 'L' and s[i+1] == 'L':
                        return False
        return True
# @lc code=end

