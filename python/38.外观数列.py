#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#
# 解法1(T41% S82%)：题目挺有意思，但代码本质就是循环和计数，因为最大的n只有30，不用考虑超时直接依次模拟就好，通过两重while循环对每个连续的相同位计数

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        say = "1"
        for i in range(2, n+1):
            tmp = ""
            i = 0
            while i<len(say):
                j = i
                while j<len(say) and say[j]==say[i]:
                    j += 1
                tmp += str(j-i) + say[j-1]
                i = j
            say = tmp
        return say
# @lc code=end

