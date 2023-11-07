# -*- coding: utf-8 -*-
# @Description: @TODO
# @Author: doubleZ
# @Date: 2023-11-07 17:14:53
# @LastEditTime: 2023-11-07 17:14:53

#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#
# 解法1(T71% S66%)：很有趣的一题，也很考验对二维数组的操作技巧，并且十分适合用python来解。旋转整张图像可以考虑成一圈圈的转，先将矩阵最外的一圈旋转，再旋转靠内的一层，如果是奇数层最终心的一个就不用旋转了，那有多少层呢？N//2层。具体某一层的旋转我们可以先考虑第一行，上面的N-2*当前层数-1个元素要移动到右面，右面的移动到下面，下面的移动到左面，左面的移动到上面，因此一重循环，循环内每次移动四个位置（记住一个数，移动三个，注意先移动再覆盖）。但python可以很方便的实现a,b=b,a，因此这四个数的转移可以一行搞定

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for loop in range(N//2):
            for i in range(N - 2*loop -1):
                matrix[loop][loop+i], matrix[loop+i][N-loop-1], matrix[N-loop-1][N-loop-1-i], matrix[N-loop-1-i][loop] = matrix[N-loop-1-i][loop], matrix[loop][loop+i], matrix[loop+i][N-loop-1], matrix[N-loop-1][N-loop-1-i]

Solution().rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
# @lc code=end

