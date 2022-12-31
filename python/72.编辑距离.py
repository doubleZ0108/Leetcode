#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#
# 解法1(T93% S40%): 动态规划
#   dp`dp[i][j]`: w1[0…i]变换为w2[0…j]需要的最少次数
#   如果i位和j位相等则不需要做操作，`dp[i][j] = dp[i-1][j-1]`
#   否则从三种操作里选最小的
#       插入：`dp[i][j] = dp[i][j-1] + 1` ，i比j少了一个字母，在结尾插入这个字母
#       删除：`dp[i][j] = dp[i-1][j] + 1` ，i比j多了一个尾字母
#       替换：`dp[i][j] = dp[i-1][j-1] + 1` ，i和j结尾不相同，替换尾字母就好了
#   初始：如果第一个单词长度为0，则需要经过j次才能变到长度为j的单词2上；反之亦然
#   最终目标：i==第一个单词长度，j==第二个单词长度
#
# 改进1(T93% S97%): 因为dp只跟前一行有关，因此不需要保留完整的二维数组，用两个一维数组dp就可以了。设定dp0代表上一行的dp结果，它需要事先做初始化，然后走两重循环，注意循环刚开始也要初始化dp1的0号元素，因为它代表着word1长度为0的情况，应该初始化为当前word2的长度j，后面的dp逻辑跟上面一样，只是分清楚哪个是上一行的用dp0，这一行的用dp1

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 解法1 改进1
        if not len(word1) or not len(word2): return max(len(word1), len(word2))

        dp0 = [0 for _ in range(len(word2)+1)]
        for j in range(1, len(word2)+1): dp0[j] = j
        dp1 = [0 for _ in range(len(word2)+1)]

        for i in range(1, len(word1)+1):
            dp1[0] = i
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp1[j] = dp0[j-1]
                else:
                    dp1[j] = min(dp0[j], dp0[j-1], dp1[j-1]) + 1
            dp0 = dp1[:]
        return dp1[-1]

    def otherSolution(self, word1, word2):
        # 解法1
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(1, len(word1)+1): dp[i][0] = i
        for j in range(1, len(word2)+1): dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
# @lc code=end

