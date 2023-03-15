#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#
# 解法1(T79% S91%)：按照题意进行两步走，第一步遍历图片的每行，将每行反转（二维数组的每行可以看作独立的一维数组），然后再两重循环遍历每个像素位置，通过1-运算来实现01反转

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i][:] = image[i][::-1]
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j] = 1 - image[i][j]
        return image
        
# @lc code=end

