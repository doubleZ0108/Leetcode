#
# @lc app=leetcode.cn id=2351 lang=python
#
# [2351] 第一次出现两次的字母
#
# 解法1(T95% S18%): 因为字符串只是由小写字母组成的，因此可以通过一个26个元素的位置数组来标识，依次遍历字符串，当有一个字母被第二次标记的时候返回这个字符即可
#   改进1(T95% S20%): 很可能好多字符压根不会出现，因此哪一个哈希表来存会节省更多的空间

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        record = [0] * 26
        for ch in s:
            pos = ord(ch) - ord('a')
            record[pos] += 1
            if record[pos] == 2:
                return ch

    def repeatedCharacter2(self, s: str) -> str:
        record = {}
        for ch in s:
            if ch not in record:
                record[ch] = 1
            else:
                return ch
# @lc code=end