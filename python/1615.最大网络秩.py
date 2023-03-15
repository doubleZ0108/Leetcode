#
# @lc app=leetcode.cn id=1615 lang=python3
#
# [1615] 最大网络秩
#
# 解法1(T5% S54%)：看了数据规模不是很大，节点不多但是边还是有点多的，两重循环所有可能的城市对没问题，但再两重循环所有边找到每个节点的度就有点大了，因此可以先通过Counter()先统计每个节点的度，要把出度和入度加在一起。之后就是两重循环所有节点，再一重循环边，看二者直接相连的边有没有被计算两次

# @lc code=start
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        cnt1 = Counter([x[0] for x in roads])
        cnt2 = Counter([x[1] for x in roads])
        cnt = cnt1
        for key, val in cnt2.items():
            if key in cnt:
                cnt[key] += val
            else:
                cnt[key] = val
    
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                this = cnt[i] + cnt[j]
                for u, v in roads:
                    if (u==i and v==j) or (v==i and u==j):
                        this -= 1
                        break
                res = max(res, this)
        return res
# @lc code=end

