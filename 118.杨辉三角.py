#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#
# 解法1(T66% S90%): 第i行应该有i个元素，首尾都是固定的1，中间项满足递推公式 x[i][j] = x[i-1][j-1] + x[i-1][j] ，也不需要考虑数组越界的问题

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]

        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            thisrow = [1]
            for j in range(1, i):
                thisrow.append(ans[i-1][j-1] + ans[i-1][j])
            thisrow.append(1)
            ans.append(thisrow)
        return ans
# @lc code=end

