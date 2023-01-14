#
# @lc app=leetcode.cn id=1819 lang=python3
#
# [1819] 序列中不同最大公约数的数目
#
# 解法1(超时 7/30+)：暴力，首先对数组去重，然后生成所有排列，再对每个排列计算gcd，但很容易也想到数组的排列有$2^n$个，肯定会超时
#     python中有很多现成的库 `combinations()` `math.gcd(*)`
# 
# 解法2(T76% S72%)：数学法，还是要想明白循环的转化，因为排列有$2^n$个，循环排列肯定会超时，但数组中元素总数最多就是$10^5$个，如果只循环数组是没问题的，又考虑到整个数组的最大公约数肯定不会超过最大那个数，所以可以从1～maxval循环，数据规模也不是很大的。具体而言，判断每个可能的最大公约数i（1～maxval）的倍数在不在原数组中，因为只有倍数的公约数才可能等于i，但只这一层约束是不够的，比如[3, 6, 10]如果循环到i=5虽然能找到10这个倍数，但原数组中没有子序列的最大公约数能为5，要至少能找到两个数使得他们的gcd确实等于当前的i（或者当前数本身就是i），那么可以放心大胆的让统计结果+1

# @lc code=start
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = set(nums)
        maxVal = max(nums)
        res = 0
        for i in range(1, maxVal+1):
            g = 0
            for x in range(i, maxVal+1, i):
                if x in nums:
                    g = math.gcd(g, x)
                    if g == i:
                        res += 1
                        break
        return res

    # 解法1 超时
    def countDifferentSubsequenceGCDs1(self, nums: List[int]) -> int:
        from itertools import combinations

        nums = list(set(nums))
        subs = []
        for i in range(1, len(nums)+1):
            subs += list(combinations(nums, i))

        res = set()
        for sub in subs:
            res.add(math.gcd(*sub))
        return len(res)
# @lc code=end

