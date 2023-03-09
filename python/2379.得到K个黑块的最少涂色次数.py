#
# @lc app=leetcode.cn id=2379 lang=python
#
# [2379] 得到K个黑块的最少涂色次数
#
# 解法1(T78% S94%)：当看到一个字符串或者数组，要求解连续多少个的问题，连续，要马上敏感的想到滑窗（为什么自己没有想到呢？真不应该），之后就简单了，依次循环每个长度为k的字符串切片，统计其中白色W有多少，把它们都变成B就可以构成连续k长度的黑色块了，Python中字符串的count()函数可以直接统计，不需要用哈希表啥的

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = blocks.count('W')
        for i in range(len(blocks)-k+1):
            res = min(res, blocks[i:i+k].count('W'))
        return res
# @lc code=end