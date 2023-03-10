#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        wordDict = set(wordDict)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                print(s[j:i])
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

# @lc code=end

