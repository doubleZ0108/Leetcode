#
# @lc app=leetcode.cn id=1626 lang=python3
#
# [1626] 无矛盾的最佳球队
#
# 解法1(T67% S43%)：本身应该是一道标准的动态规划，但是要解构题干整理成dp的样子，先把score和age打包成元组并对score排序，这样能保证后面的人比前面的人得分高，那再来一重dp内的循环比较年龄就可以，如果之前的一个人j年龄比我小，那我跟他都可以被选，dp[i] = max(dp[i], dp[j]+data[i][0]) for j in range(i)，记得data已经是打包了元组并进行排序的，因此不能直接再访问scores[i]

# @lc code=start
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        data = sorted(zip(scores, ages))
        dp = [0 for _ in range(len(ages))]
        for i in range(len(data)):
            for j in range(i):
                if data[i][1] >= data[j][1]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += data[i][0]
        return max(dp)
# @lc code=end

