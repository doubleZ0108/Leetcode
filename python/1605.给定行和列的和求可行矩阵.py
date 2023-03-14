#
# @lc app=leetcode.cn id=1605 lang=python3
#
# [1605] 给定行和列的和求可行矩阵
#
# 解法1(T50% S40%)：题不难，就是之前没见过，先构建一个空的row x col维度的矩阵，两重循环(i, j)，每个矩阵元素取min(rowSum[i], colSum[j])，该行和该列的和rowSum[i], colSum[j]再减去这个数即可。本质就是一个贪心选取的策略，大不了最后全为0

# @lc code=start
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        if len(rowSum)==1 and len(colSum)==1: return [rowSum]
        res = [[0]*len(colSum) for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        return res
# @lc code=end

