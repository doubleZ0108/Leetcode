#
# @lc app=leetcode.cn id=746 lang=python
#
# [746] 使用最小花费爬楼梯
#
# 解法1: 动态规划，维护dp数组，每个元素是走到当前这步的最小花费，需要注意最终返回的是min(最后一个台阶，倒数第二个台阶)
#   改进1: 与基础爬楼梯方法相同，只是用两个变量进行迭代
#   改进2(T80% S94%): dp数组直接用原数组进行，完全不需要任何新空间

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])

        return min(cost[-2:])
# @lc code=end

