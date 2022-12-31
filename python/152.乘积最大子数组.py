#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#
# 解法1(T97% S45%): 如果一个子列中负数有偶数个，那所有数乘起来就是最大值；如果负数有奇数个，那从最左一直乘到最后一个负数最大 或者从右一直乘到最前一个负数最大；但如果出现0就会直接归零。因此这个问题就是被0划分的每个小数组中做负数奇偶的讨论，可以通过dp从左到右 从右到左各做一次，取max(max(左→右), max(右→左))
# 
# 解法2(T90% S22%): 这题跟300题不一样之处在于，加法如果加上一个负数一定是不好的，所以只累计正数就完了，但对于乘法很可能现在成了个负数，一会还要乘个负数，结果是更大的。所以要分开讨论dp数组的变化
#   如果当前`num[i]>0`，则希望前一段的乘积尽可能大
#   如果当前`num[i]<0`，则希望前一段的乘积尽可能小 
# 因此需要定义两个dp数组，`dp_max[i]`代表以第i个数结尾的连续子数组乘积的最大值，`dp_min[i]`代表以第i个数结尾的连续子数组乘积的最小值，每次两个dp数组都进行扩展，最后选择`dp_max`中最大值

import copy
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

    def otherSolution(self, nums):
        # 解法2
        dp_max = copy.copy(nums)
        dp_min = copy.copy(nums)

        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])

        return max(dp_max)

# @lc code=end

