#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#
# 解法1(T85% S79%)：没什么技巧，双重循环，外层循环每个字符串，内层依次比较两字符串的各位是否相等，整体通过一个值记录当前的最小值，可以以此作为内层的提前终止条件

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minLength = len(strs[0])
        for i in range(1, len(strs)):
            j = 0
            while j<len(strs[i]) and j<minLength and strs[i][j]==strs[i-1][j]: j += 1
            minLength = min(minLength, j)
        return strs[0][:minLength]
# @lc code=end

