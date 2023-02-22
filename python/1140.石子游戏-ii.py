#
# @lc app=leetcode.cn id=1140 lang=python3
#
# [1140] 石子游戏 II
#
# 解法1(T30% S100%)：这题一看就很不好想，轮流着拿，每次越拿越可以拿的很多，但肯定不是贪心的全拿，还要尽可能的让对方少拿，这么想起来就很乱完全没法做。但仔细想这种结构肯定是用动态规划来处理，先把能确定的结果确定然后一点一点的扩展到一般情况，我们能确定的是什么呢？如果游戏已经进行到很后面了，我当前能拿的最大数量是2M个，但当前位置之后没有那么多石头了，那就意味着我可以一次把所有剩下的石头都拿走，这肯定是一个最优解。所以发现本题应该是从后往前动态规划处理，最终目标是下标位0且M=1时的解。m的循环到1就可以了，不存在m=0的情况。
#     dp[i][m]代表当前站在i位置，M=m，我能拿的石头数量是1~2m个
#     if 2m ≥ n-i，也就是按照上面说的，如果我能一次把剩下所有石头都拿走那就全拿了，此时的dp值是sum(piles[i:])，即剩下所有石头的和（后缀和）
#     else，我当前可以拿1~2m个，但是无论怎么拿还要进行下一轮让对方拿，那我的策略是尽可能让对方下轮的分数低，反过来想也就是让我在当下尽可能拿的多。因为我并不知道拿多少个最好，所以只能循环我的所有可能情况1~2m，对于一个我选定的数量x，对手下一局的成绩是什么呢？对手在i+x之后的位置里 他那时的M是我此时选定的这个x和我当前的m的最大值，即dp[i+x][max(m,x)]，这个是真的不太好想
#     最终目标就是dp[0][1]也就是题干

# @lc code=start
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        if len(piles) <= 2: return sum(piles)

        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        tailsum = 0
        for i in range(n-1, -1, -1):
            tailsum += piles[i]
            for m in range(n-1, 0, -1):
                if 2*m >= n-i:
                    dp[i][m] = tailsum
                else:
                    for x in range(1, 2*m+1):
                        dp[i][m] = max(dp[i][m], tailsum-dp[i+x][max(m,x)])
        return dp[0][1]
# @lc code=end

