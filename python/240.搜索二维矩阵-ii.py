#
# @lc app=leetcode.cn id=240 lang=python
#
# [240] 搜索二维矩阵 II
#
# 解法1(T35% S82%): 正常遍历二维数组中加入提前终止条件：如果某行第一个元素就比target大，可以直接结束返回没找到；某行某列的元素大于target，这一行后面的列可以不用看了
# 
# 解法2(T88% S96%)：从右上角来看就是一棵二叉搜索树，如果当前节点比target小，去右子树（行+1）；如果比target大，去左子树（j-1）
# 
# 解法3: 之字形遍历，但会遇到这么几个问题：第一，每一个斜边必须完全遍历完才能断定是不是所有数都比target大也才能决定是否提前终止；第二，遍历逻辑有点复杂，并不像想象中的i+j=num就可以

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 解法2
        i, j = 0, len(matrix[0])-1
        while i<len(matrix) and j>-1:
            if matrix[i][j] == target: return True
            elif matrix[i][j] < target: i += 1
            else: j -= 1
        return False

    def otherSolution(self, matrix, target):
        # 解法1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                break
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break

        return False
# @lc code=end

