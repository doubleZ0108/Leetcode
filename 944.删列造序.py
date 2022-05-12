#
# @lc app=leetcode.cn id=944 lang=python
#
# [944] 删列造序
#
# 解法1(T60% S38%)：没什么好说的，纯数组遍历的题，也没什么坑，两重循环解决

# @lc code=start
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = 0
        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if i == 0: continue
                if strs[i][j] < strs[i-1][j]:
                    res += 1
                    break
        return res
# @lc code=end

