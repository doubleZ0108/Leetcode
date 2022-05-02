#
# @lc app=leetcode.cn id=219 lang=python
#
# [219] 存在重复元素 II
#
# 解法1(T78% S60%): 还是通过哈希表，value保存下标，如果满足绝对距离小于k则返回，否则更新key的value下标。 为什么可以不用数组保存所有下标呢？因为如果之前的绝对距离太大不满足条件，可以放心大胆的舍弃换成最近的

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = {}
        for i in range(len(nums)):
            if nums[i] not in table: table[nums[i]] = i
            else:
                if abs(i-table[nums[i]]) <= k: return True
                else: table[nums[i]] = i
        return False
# @lc code=end

