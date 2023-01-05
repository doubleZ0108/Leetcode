#
# @lc app=leetcode.cn id=1803 lang=python3
#
# [1803] 统计异或值在范围内的数对有多少
#
# 解法1(超时 41/63)：朴素的想法肯定是双重循环暴力求解，但看看问题规模肯定会超时
# 解法2(py3超时 41/63 ｜JS可以通过更多59/63)：
    
# 同样是双重循环暴力求解，但是考虑到数组nums大都很大很大，循环N*(N-1)次是在太容易超时，但low~high这个区间不一定很大，或者说一般都可以接受。 
#   > 恰好异或还有一个非常好的性质：x ^ y = t <=> x ^ t = y。 
#   > 原来问题可以看做找数组中的两个数x和y，如果他们的异或值t在给定的low～high范围内则总数+1，根据这个性质，可以把问题看作数组中的每个数x，它跟low~high中的每个数t做异或得到y，如果y恰好在原数组中，则证明找到一个数组对x和y。
#   > 还有一件事情要想明白，nums没说每个数彼此不同，某个数可能出现非常多变，但虽然nums[i]相同，但对应的下标i肯定不同，要算做不同的对，因此很有必要统计一下每个数出现了多少遍，这样如果找到了一个匹配的x和y，再乘以x的数量就又可以节省很多计算了。
# 
#   说完了这些性质和想法，就要说具体思路了：首先统计nums中每个数出现的频次（可以通过哈希表或是一个countarr），对于nums中的每个数x，计算x和low~high中每个数t的异或值，如果x^t在nums中，则证明存在这样的x和y=x^t，使得他们的异或值t在规定的范围内，整体sum加和起来即可
# 
#   看到C++和Java是可以踩线通过的，但是python3和javascript都还是会超时
# 
#    改进1(T27% S5%): 用numpy来加速
#        枚举low～high中的每个数：`np.arange(low, high+1)` 这个还是能想到的
#        统计nums中每个数出现的次数：不用哈希表或者Counter()，numpy中有`bincount()`，可以简单理解为在二进制的语境下统计每个数出现的次数，因此要给顶二进制的最大位数，可以通过bit_length统计所有数字中最大的二进制位数要用多少位
#       循环也可以通过列表生成式和聚合函数来做，整体代码一场简洁（简介可不一定是好事啊，往往恰恰相反…）

# @lc code=start
class Solution:
    # 解法1 暴力求解 超时
    def countPairs1(self, nums: List[int], low: int, high: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                tmp = nums[i] ^ nums[j]
                if tmp >= low and tmp <= high: 
                    res += 1
        return res

    # 解法2
    def countPairs2(self, nums: List[int], low: int, high: int) -> int:
        cnt = Counter(nums)
        res = 0
        for x in cnt.keys():
            for t in range(low, high+1):
                res += cnt[x] * cnt[x^t]
        return res//2

        # # 解法2 的另一种写法，本质是一样的
        # cnt = [0 for _ in range((2*10**4))]
        # for num in nums:
        #     cnt[num] += 1
        # res = 0
        # for x in range(min(nums), max(nums)+1):
        #     if cnt[x] > 0:
        #         for t in range(low, high+1):
        #             res += cnt[x] * cnt[x^t]
        # return res//2

    def countPairs2_(self, nums: List[int], low: int, high: int) -> int:
        # 所有数字中二进制最大需要多少位表示
        maxBits = max(max(x.bit_length() for x in nums), low.bit_length(), high.bit_length())
        # np.bincount() 简单来说是统计nums中每个数出现的次数，当然是在二进制的语境下统计的
        # minlength 最少展开的二进制位数 2^numBits
        cnt = np.bincount(nums, minlength=(1<<maxBits))
        # 合理区间内的每个数，本题无非就是找x^y == 合理区间中的每一个数 的总(x,y)对数
        targets = np.arange(low, high+1)
        # 利用异或的性质 x^y = xor => x^xor = y，因为freq包含了y出现的频次，如果y在某位没出现，则x^y也不可能等于targets中的那个数，也就是说没有数对的异或等于这个数，完全统计low~high中的每个数也就求得到总数
        return int(sum([cnt[targets^x].sum() for x in nums]) // 2)
            
    
# @lc code=end

