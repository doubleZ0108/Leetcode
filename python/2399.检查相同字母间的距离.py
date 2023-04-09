#
# @lc app=leetcode.cn id=2399 lang=python
#
# [2399] 检查相同字母间的距离
# 
# 解法1(T95% S93%)：因为题目保证了每个字母在s中出现且仅出现2次，因此我们可以通过set()很方便的到底是有那几个字母，对于这几个字母判断是否满足distance就好，而找到二者的距离可以通过查找函数进行，index()从左往右查找第一个出现的位置，rindex()从右往左找第一个的位置

# @lc code=start
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        waits = list(set(s))
        for wait in waits:
            if s.rindex(wait) - s.index(wait) - 1 != distance[ord(wait)-ord('a')]:
                return False
        return True
# @lc code=end