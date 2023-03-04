#
# @lc app=leetcode.cn id=982 lang=python3
#
# [982] 按位与为零的三元组
#
# 解法1(T23% S5%)：这题属于是被唬住了，看到困难和按位与，马上想到可能是要利用&的性质来做，即a&a=0，也就是说只要有两个相同的数结果就一定为0，但毕竟这是三元组三个数不一定非要有两个相同才能等于0。看了下题解才翻然悔悟，求三元组，那最多也才三重循环，题目的最大长度是1000，1000^3确实会超时但稍微优化一点还是很有希望的。这种优化手段之前好像有道题用过，暂时没想起来是哪道，我们先用两重循环把两个数nums[i] & nums[j]算完存下来，因为他俩的与运算会有很多重复值，每一个相同的数再与第三个数nums[k]求与结果肯定相同，因此可以通过Counter()做统计，这样就从一个一个统计变成了一组一组统计，求与运算显然会有很多很多重复，因此这样会加速很多

# @lc code=start
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt_ij = Counter([i&j for i in nums for j in nums])
        res = 0
        for k in nums:
            for ij, freq in cnt_ij.items():
                if k & ij == 0:
                    res += freq
        return res

# @lc code=end

