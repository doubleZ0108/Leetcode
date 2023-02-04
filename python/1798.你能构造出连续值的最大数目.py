#
# @lc app=leetcode.cn id=1798 lang=python3
#
# [1798] 你能构造出连续值的最大数目
#
# 解法1(超时 5/72)：全排列暴力模拟
# 解法2(超时 10/72)：回溯，同样给出0～sum(coins)每个位置的可能
# 解法3(T87% S86%)：解法1 2都是对题目理解错了（p.s. 实在容易让人混淆），题目的意思是结果必须是从0开始的连续整数，中间一段的不行。所以这个问题肯定不能暴力模拟，因为很多计算都是没用的，我们来想，最终的结果肯定是我们能构建[0, x]范围内的数，最开始我们只能构建0一个数，新来一个数coin（排序一下），我们的范围会被更新到[coin, coin+x]，但如果新区间的左端点coin超出了之前的右端点x很多，那就不连续了所以就可以终止了，否则的话区间右端点就自然的加上这个coin变大即可

# @lc code=start
class Solution:
    # 解法3
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        res = 0
        for coin in coins:
            if coin > res + 1:
                break
            else:
                res += coin

        return res+1


    def getMaximumConsecutive1(self, coins: List[int]) -> int:
        dp = [False for _ in range(sum(coins)+1)]

        # 解法1
        for i in range(len(coins)+1):
            for perm in itertools.permutations(coins, i):
                dp[sum(perm)] = True

        # 解法2
        # def deepin(idx, parts):
        #     if idx >= len(coins):
        #         dp[parts] = True
        #         return
        #     deepin(idx+1, parts+coins[idx])
        #     deepin(idx+1, parts)
        
        # deepin(0, 0)

        maxLength = 0
        for d in dp:
            if not d:
                break
            maxLength += 1
        return maxLength
# @lc code=end

