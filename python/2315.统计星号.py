#
# @lc app=leetcode.cn id=2315 lang=python
#
# [2315] 统计星号
#
# 解法1(T93% S73%)：没啥好说的，通过一个变量flag刻画两竖线内的范围，初始化为false，遇到第一个竖线变为true，再遇到第二个变回false，统计flag为false时遇到的*即可

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        flag = False
        for ch in s:
            if not flag and ch=='*':
                res += 1
            elif flag and ch=='|':
                flag = False
            elif not flag and ch=='|':
                flag = True
        return res
# @lc code=end