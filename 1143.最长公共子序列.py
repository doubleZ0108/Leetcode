#
# @lc app=leetcode.cn id=1143 lang=python
#
# [1143] 最长公共子序列
#
# 解法1(T94% S84%): 动态规划。代码异常简单，想法还是比较费劲。
#   定义`dp[i][j]`代表text1[:i]和text2[:j]两个子序列的最长公共子序列长度
#   状态转移方程：
#       if text1[i] == text2[j], `dp[i][j] = dp[i-1][j-1]+1`，这个比较好理解，如果之前的已经求出来了，当前这位两字符还一样，那很自然的公共子序列长度又大了1
#       else, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`，从上面和左面进行扩展，因为这一位两字符不想等，所以要么是text1考虑全，text2不考虑当前这位的公共子序列最长，要么由于对称反过来，核心在于比当前长度短的子序列的最长公共长度已经求出来了

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(text1)][len(text2)]
# @lc code=end

