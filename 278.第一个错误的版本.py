#
# @lc app=leetcode.cn id=278 lang=python
#
# [278] 第一个错误的版本
#
# 解法1(T88% S25%)：标准二分查找，如果中值不是错误版本，证明错误的肯定在后一半；如果中值是错误版本，当前版本和之前的都有可能是错误，因此right只能缩到mid，同时要加判断，如果前后两次mid相同，则证明它就是第一个错误的版本

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if mid == right: break
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return mid
        
# @lc code=end

