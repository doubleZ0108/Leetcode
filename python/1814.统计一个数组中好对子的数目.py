#
# @lc app=leetcode.cn id=1814 lang=python3
#
# [1814] 统计一个数组中好对子的数目
#
# 解法1(超时 64/84)：暴力+缓存。首先把每个数的rev都算出来存一下，要不然会重复计算浪费时间，然后两重循环来累积。想想就肯定会超时，因为数据规模有$10^5$，两重循环肯定会炸
#
# 解法2(T100% S2.5%)：我们来看题设的条件`nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])` ，其实很容易想到左右等式移下项，`nums[i] - rev(nums[i]) == nums[j] + rev(nums[j])`，我们不妨令`T[i] = nums[i] - rev(nums[i])`，那问题就变得很简单了，也就是找T数组中相等元素的个数。所以我们先制作T数组，然后对它用哈希表进行元素频次的统计，最后一重循环，如果某个数出现了n次，则对数有$C_n^2 = \frac{n(n-1)}{2}$个，当然n至少要有2个才能组成一对。

# @lc code=start
class Solution:
    # 解法2
    def countNicePairs(self, nums: List[int]) -> int:
        T = [x-int(str(x)[::-1]) for x in nums]
        freqs = Counter(T)
        
        res = 0
        for val in freqs.values():
            if val > 1:
                res += val*(val-1)//2
        return res%(10**9+7)

    # 解法1 超时
    def countNicePairs1(self, nums: List[int]) -> int:
        res = 0
        rev_nums = [int(str(x)[::-1]) for x in nums]
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+rev_nums[j] == nums[j]+rev_nums[i]:
                    res += 1
        return res%(10**9+7)
# @lc code=end

