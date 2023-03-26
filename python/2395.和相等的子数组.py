#
# @lc app=leetcode.cn id=2395 lang=python
#
# [2395] 和相等的子数组
# 
# 解法1(T56% S9%)：一次遍历，通过一个集合存储已经计算得到的值，如果两个相邻的数求和在集合中则True，否则将其添加入集合

# @lc code=start
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        store = set()
        for i in range(1, len(nums)):
            tmp = nums[i-1] + nums[i]
            if tmp in store:
                return True
            else:
                store.add(tmp)
        return False
# @lc code=end