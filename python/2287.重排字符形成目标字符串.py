#
# @lc app=leetcode.cn id=2287 lang=python3
#
# [2287] 重排字符形成目标字符串
#
# 解法1(88% 51%)：因为只有26个小写字母，因此很容易想到通过哈希表或者比特数组先分别统计下两字符串每个字符都出现了多少次，然后一次遍历两数组中的各位，如果t在这个字符有，但s没有则直接返回0，此时不可能有副本；否则就计算s//t并全局取最小值即可

# @lc code=start
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        bits_s = [0 for _ in range(26)]
        bits_t = [0 for _ in range(26)]
        for ch in s:
            bits_s[ord(ch) - ord('a')] += 1
        for ch in target:
            bits_t[ord(ch) - ord('a')] += 1

        res = float('inf')
        for bs, bt in zip(bits_s, bits_t):
            if bt != 0:
                if bt>bs: 
                    return 0
                else:
                    res = min(res, bs//bt)
        return res
# @lc code=end

