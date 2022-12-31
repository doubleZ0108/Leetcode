#
# @lc app=leetcode.cn id=220 lang=python
#
# [220] 存在重复元素 III
#
# 解法1(超时): 双重循环，第二重循环考虑下标左右两边k的长度
# 
# 解法2(T54% S8%): 桶排序（计数排序），首先将原数组按照值进行排序并保存下标，然后外层一次遍历，内层从当前遍历向前试探，如果找到 下标≤k & 满足值≤t 则返回True，如果这两个条件都没满足则代表后面的也不可能满足了，break再往前遍历一个新位置

# @lc code=start
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not len(nums): return False

        army = sorted(enumerate(nums), key=lambda x: x[1])
        for i in range(1, len(nums)):
            j = i
            while j<len(nums):
                if abs(army[i-1][0]-army[j][0])<=k and abs(army[i-1][1]-army[j][1])<=t: return True
                elif abs(army[i-1][0]-army[j][0])>k and abs(army[i-1][1]-army[j][1])>t: break
                j += 1

        return False  

# @lc code=end

