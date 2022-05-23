#
# @lc app=leetcode.cn id=720 lang=python
#
# [720] 词典中最长的单词
#
# 解法1(T92% S52%)：先按照字符串长度排序，利用一个set()，一次遍历：如果单词长度为1 or 当前字符串去掉最后一位在set中，则代表该字符串的前序一定在词典中，则把当前单词也加入set并更新是否为最长的。为什么要排序呢，因为要满足一次只多一个字符，如果是只有a abc是不满足的

# @lc code=start
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words_sorted = sorted(words)
        maxStr = ""
        myset = set()
        for word in words_sorted:
            if len(word) == 1 or word[:-1] in myset:
                myset.add(word)
                if len(word) > len(maxStr): maxStr = word
        return maxStr
        
# @lc code=end

