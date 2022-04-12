#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#
# 解法1(T97% S45%): 如果一个子列中负数有偶数个，那所有数乘起来就是最大值；如果负数有奇数个，那从最左一直乘到最后一个负数最大 或者从右一直乘到最前一个负数最大；但如果出现0就会直接归零。因此这个问题就是被0划分的每个小数组中做负数奇偶的讨论，可以通过dp从左到右 从右到左各做一次，取max(max(左→右), max(右→左))

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        revs = nums[::-1]
        for i in range(1,len(nums)):
            nums[i] *= nums[i-1] if nums[i-1]!=0 else 1     # 如果前一位是0，i就相当于新的开始，这位的dp就是它自己，所以*=1，否则无脑乘上前面就好
        for i in range(1,len(revs)):
            revs[i] *= revs[i-1] if revs[i-1]!=0 else 1

        return max(max(nums), max(revs))

# @lc code=end

