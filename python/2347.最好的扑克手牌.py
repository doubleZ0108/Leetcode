#
# @lc app=leetcode.cn id=1154 lang=python
#
# [2347] 最好的扑克手牌
#
# 解法1(T13% S56%)：没啥好说的，按照题意从上到下一个一个情况判断就好，判断有几张想等的牌可以直接通过哈希表统计来做，需要注意的是三条只要大于3张相同都可以，题里说的不是太清楚

# @lc code=start
class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        if len(set(suits)) == 1: return "Flush"
        cnt = Counter(ranks)
        for key, val in cnt.items():
            if val >= 3: return "Three of a Kind"
        for key, val in cnt.items():
            if val == 2: return "Pair"
        if len(cnt.keys()) == 5: return "High Card"
# @lc code=end