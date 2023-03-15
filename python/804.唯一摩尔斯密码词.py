#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#
# 解法1(T53% S53%)：遍历每个单词的每个字符，依次将每个单词的所有字母转换为对应的摩尔斯密码，最后通过一个集合来维护不同的结果，返回集合的长度即可

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        D = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for word in words:
            tmp = ""
            for ch in word:
                tmp += D[ord(ch)-ord('a')]
            res.add(tmp)
        return len(res)
# @lc code=end

