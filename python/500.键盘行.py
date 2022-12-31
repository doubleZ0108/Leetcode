#
# @lc app=leetcode.cn id=500 lang=python
#
# [500] 键盘行
#
# 解法1(T64% S33%): 很朴素，就是每个单词的每个字母依次判断在哪行里，如果同一个单词的所有字母都在同一行里就加到结果中（通过flag和break控制）
# 
# 解法2(T98% S60%)：python库函数，通过`strip()`把word中所有第x行字符删掉，如果能删干净那证明这个word的所有字符都在同一行里

# @lc code=start
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for word in words:
            lword = word.lower()
            if not lword.strip("qwertyuiop") or not lword.strip("asdfghjkl") or not lword.strip("zxcvbnm"):
                res.append(word)
        return res


    def otherSolution(self, words):
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for word in words:
            flag = True
            our = -1
            for l in word:
                for row in keyboard:
                    if l.lower() in row:
                        if our != -1 and row != our:
                            flag = False
                            break
                        our = row
                if not flag:
                    break

            if flag:
                res.append(word)

        return res
# @lc code=end

