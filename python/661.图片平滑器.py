#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#
# 解法1(65% S16%)：很典型的二维数组循环的题，不要吝惜使用数组存储候选值candidate，数据结构和存储就是为了方便我们处理问题的，之后9个数不要不舍得存，直接对每个像素循环周围的9个数，如果在边界内则加入candidate数组，然后直接求数组的平均值就好。不引入这个数组的话就要写很多if-else，而且如果不是3*3filter扩展性还不好

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cands = []
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x>=0 and y>=0 and x<m and y<n:
                            cands.append(img[x][y])
                res[i][j] = sum(cands) // len(cands)
        return res
# @lc code=end

