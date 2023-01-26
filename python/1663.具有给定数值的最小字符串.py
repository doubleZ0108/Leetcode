#
# @lc app=leetcode.cn id=1663 lang=python3
#
# [1663] 具有给定数值的最小字符串
#
# 解法1(超时 13/94)：回溯，很直观，我需要不断探索不断将字母加入并判断是否合法，这十分满足回溯法的结构。递归函数的变量定义为当前字符串结果，剩余位数l，剩余数值remain，初始l=n, remain=k，当剩余位数和剩余数值刚好用完时返回结果，否则如果二者有人为0了就代表这种组合不可能（要么是数值超了，要么是位数超了），接下来就在合理的字母范围内进行递归搜索。这种方法也很明显，数据规模有$10^5$显然会超时
#
# 解法2(T5% S58%)：贪心，再仔细想一下本题的问题，最终输出的肯定是个n位的字符串，而且每位的字符都应该尽可能小，优点贪心的味道，比如前n-1位都取a，最后一位按照规定的数值取（假设正好在26以内），那这样的字符串一定是字典序最短的（‼️因为无论怎样结果都一定是n位，这点要想清楚）。现在我们来讨论一下贪心的子结构，如图所示，第i位的时候，前i-1位已经决定完了，剩下了数值k，贪心告诉我们当后面n-i-1位都取z的时候，我能取到最小，但如果后面都取z很可能数值不够了，因此第i位的下限就是1

# @lc code=start
class Solution:
    # 解法2
    def getSmallestString(self, n: int, k: int) -> str:
        res = ""
        for i in range(n):
            val = max(1, k - (n-i-1)*26)
            k -= val
            res += chr(int(val)+ord('a')-1)
        return res


    # 解法1 超时
    def getSmallestString1(self, n: int, k: int) -> str:
        res = []

        def deepin(strs, l, remain):
            if l==0 and remain==0:
                res.append(strs)
                return True
            if l==0 or remain==0:
                return False
            for i in range(1, min(remain+1, 26+1)):
                if deepin(strs+[i], l-1, remain-i):
                    return
              
        deepin([], n, k)
        return "".join([chr(ch+ord('a')-1) for ch in res[0]])


Solution().getSmallestString(3, 27)
# @lc code=end

