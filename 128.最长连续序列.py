#
# @lc app=leetcode.cn id=128 lang=python
#
# [128] 最长连续序列
#
# 解法1(超时)：先把每个数存入哈希表，这样查找的复杂度就是$O(1)$，一次遍历，如果num-1在哈希表里则pass，因为肯定有比它更小的，到时候它那条才是最长的；如果不在则不断试探num+1是否在哈希表里，获取当前长度再选出最长
#   改进1：如果`当前num+当前最大长度`不在哈希表里，那这次循环就不用看了
#   改进2(T97% S43%): 不要用pass，直接采用not的条件，否则会影响性能emmm

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = set(nums)
        maxlength = 0
        for num in nums:
            # 这样pass会超时
            # if (num-1) in table: pass
            # if (num+maxlength) not in table: pass

            if num-1 not in table and num+maxlength in table:
                thislength = 1
                while (num+1) in table:
                    thislength += 1
                    num += 1
                if thislength > maxlength:
                    maxlength = thislength
        return maxlength
# @lc code=end

