#
# @lc app=leetcode.cn id=1638 lang=python3
#
# [1638] 统计只差一个字符的子串数目
#
# 解法1(T32% S68%)：说实话没太看懂这道题要干什么，整体做法就是枚举两个字符串中素有位置，然后再来一重循环判断是否在某处只有一个不同，如果是则统计结果加一，如果超过一处不同就停止搜索

# @lc code=start
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(len(t)):
                k = 0
                diff = 0
                while i+k<len(s) and j+k<len(t):
                    if s[i+k] != t[j+k]:
                        diff += 1
                    if diff == 1:
                        res += 1
                    elif diff > 1:
                        break
                    k += 1
        return res
# @lc code=end

