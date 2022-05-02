#
# @lc app=leetcode.cn id=217 lang=python
#
# [217] 存在重复元素
#
# 解法1(T38% S65%): 哈希表一次循环解决没什么好说的
# 
# 解法2(T68% S46%): 用集合set去重，如果去完重变短了则证明有重复元素

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) < len(nums)

    def otherSolution(self, nums):
        table = {}
        for num in nums:
            if num in table: return True
            table[num] = 1
        return False
# @lc code=end

