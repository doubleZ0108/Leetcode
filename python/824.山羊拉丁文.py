#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#
# 解法1(T46% S96)：根据题干描述写代码就好，首先将字符串根据空格划分成数组方便遍历，对于每一个单词如果是辅音开头则先把开头移动到最后（可以通过数组切片来做，要不然只能一次循环配合tmp了），然后添加ma并添加一定数量的a，最终再将单词拼接成空格分隔的语句就好

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        S = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(len(words)):
            if words[i][0].lower() not in S:
                words[i] = words[i][1:]+words[i][0]
            words[i] += "ma" + "a"*(i+1)
        return " ".join(words)
# @lc code=end

