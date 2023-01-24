#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#
# 解法1(可能超时)：代码写起来还是有点绕的，当我站在一个位置，不断向前探索跟当前位一样的元素，并计数cnt，然后再不断探索跟当前位不同的元素，同一个计数器不断递减，如果计数器恰好为零了则代表中间的0和1正好连续且匹配，此时结果加一，我可以再向前一步
#     改进1(T6% S77%)：在cnt≥0的前提下，直接就相当于找到了cnt对结果，此时我的位置可以一下子跳过cnt个，从下一个不同的数开始，不需要一点一点试探

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        i = 0
        while i<len(s):
            j = i
            cnt = 0
            while j<len(s) and s[j]==s[i]:
                cnt += 1
                j += 1
            k = j
            while k<len(s) and s[k]!=s[i] and cnt>0:
                cnt -= 1
                k += 1

            res += j-i-cnt
            i = j

        return res
# @lc code=end

