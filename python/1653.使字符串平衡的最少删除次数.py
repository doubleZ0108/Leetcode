#
# @lc app=leetcode.cn id=1653 lang=python3
#
# [1653] 使字符串平衡的最少删除次数
#
# 解法1(T48% S98%)：因为只有两个字符，那无非是删a还是删b的事，当某个位置左侧没有b且右侧没有a则代表平衡，我们模拟所有这样的位置，计算这个位置左边的b和右面的a的总个数即可，问题转换成了前缀和后缀问题，首先先统计a的后缀次数，b的前缀次数肯定为0，从头到尾模拟所有位置，计算每个位置左边b和右面a的总个数，选最小值即可
#     需要注意的一点是结果最开始不能初始化为s的长度，因为最大可能就是站在开始把所有a都删了，如果初始化为s的长度，全b的样例会有问题

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        righta, leftb = s.count('a'), 0
        res = righta+leftb  # 不能初始化为len(s) 全b的序列会错
        for ch in s:
            if ch == 'a':
                righta -= 1
            else:
                leftb += 1
            res = min(res, righta+leftb)
        return res
# @lc code=end

