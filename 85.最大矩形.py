#
# @lc app=leetcode.cn id=85 lang=python
#
# [85] 最大矩形
#
# 解法1(T13% S88%): 动态规划（嵌套一层循环的dp）。思想其实并不复杂，每一个位置看看它能达到的向上最大高度和向左最大宽度，这可以通过一个`dp`来求，假设获取了这个信息，只需在这个点往左的宽度内依次遍历，每个位置向上取最小高度，并依次计算面积，最终保留最大值即可
#   而dp是如何做的呢？可以用两个dp数组分别来做（实测比把两个数组变为一个消耗内存少）
#   dp_top[i][j] = dp_top[i-1][j] + 1
#   dp_left[i][j] = dp_left[i][j-1] + 1

# @lc code=start
from numpy import mat


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])

        dp_top = [[0]*(n+1) for _ in range(m+1)]
        dp_left = [[0]*(n+1) for _ in range(m+1)]

        maxArea = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == "1":
                    dp_top[i][j] = dp_top[i-1][j]+1
                    dp_left[i][j] = dp_left[i][j-1]+1

                    minHeight = dp_top[i][j]
                    for k in range(j, j-dp_left[i][j], -1):
                        width = j-k+1
                        minHeight = min(minHeight, dp_top[i][k])
                        maxArea = max(maxArea, minHeight*width)

        return maxArea

        
Solution().maximalRectangle([["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]])
