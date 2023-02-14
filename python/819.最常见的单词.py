#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#
# 解法1(T89% S43%)：是一道很完整的字符串处理的题。首先分词不能直接对空格或是标点split()，因为有一些特殊的测试用例，因此还是老老实实根据标点和空格利用双重循环和数组切片划分字符串为数组，然后通过哈希表统计每个词出现的频次并排序，最后再一重循环找到第一个不在ban里的单词。注意标点和禁用列表都应该转化为set()加速查找

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        puncs = set([_ for _ in "!?',;."])
        banned = set(banned)
        words = []
        i = 0
        while i<len(paragraph):
            j = i+1
            while j<len(paragraph) and paragraph[j]!=' ' and paragraph[j] not in puncs:
                j += 1
            words.append(paragraph[i:j].lower())
            i = j+1
            while i<len(paragraph) and (paragraph[i]==' ' or paragraph[i] in puncs):
                i += 1
        print(words)
        
        cnt = sorted(Counter(words).items(), key=lambda x: x[1])[::-1]
        for key, val in cnt:
            if key not in banned:
                return key
# @lc code=end

