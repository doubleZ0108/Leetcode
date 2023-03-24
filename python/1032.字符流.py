#
# @lc app=leetcode.cn id=1032 lang=python3
#
# [1032] 字符流
#
# 解法1(T11% S92%)：本来看到困难又想放弃了，但直接按照题意写居然一次就过了。具体而言类中维护一个words的集合加速查找，再维护一个单词的最大长度，如果后缀超过这个长度就不用继续找了，再通过一个字符串维护流中的所有字符。读取一个字符将其放在字符串后面，然后从后往前一次循环进行切片并判断是否在集合中即可

# @lc code=start
class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.maxLen = max([len(x) for x in words])
        self.sentense = ""


    def query(self, letter: str) -> bool:
        self.sentense += letter
        for i in range(len(self.sentense)-1, max(len(self.sentense)-1-self.maxLen, -1), -1):
            if self.sentense[i:] in self.words:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# @lc code=end

