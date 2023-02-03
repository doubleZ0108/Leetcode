#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#
# 解法2(T5% S5%)：直接借助np.reshape()，但结果要tolist()转换可能耗费了很多时间

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np
        if len(mat)*len(mat[0]) != r*c:
            return mat
        else:
            return np.reshape(mat, (r, c)).tolist()
# @lc code=end

