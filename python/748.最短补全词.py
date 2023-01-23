#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#
# 解法1(T54% S12%)：纯字符串处理题，不过还是有点小麻烦的。首先把原字符串进行过滤，滤掉空格和数字并转为字符数组进行排序（方便python处理），然后循环words，对于每个word先排序，然后用双指针来判断word是否包含了license里所有的字符，最后保存最小的结果就好。双指针判断可以参考 392题. 判断子序列

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = sorted(list(filter(lambda x: not (ord(x)>=ord('0') and ord(x)<=ord('9')) and x!=' ', [_ for _ in licensePlate.lower()])))
        residx = -1
        for idx, word in enumerate(words):
            strs = sorted([_ for _ in word])
            i, j = 0, 0
            while i<len(licensePlate) and j<len(strs):
                if licensePlate[i] == strs[j]:
                    i += 1
                    j += 1
                else:
                    while j<len(strs) and licensePlate[i] != strs[j]:
                        j += 1
            if i==len(licensePlate):
                if residx==-1 or len(word)<len(words[residx]):
                    residx = idx
        return words[residx]
# @lc code=end

