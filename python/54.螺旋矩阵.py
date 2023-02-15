#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# 解法1(T66% S92%)：这种对二维数组特殊遍历的题都很考验对二维循环变量的理解，在纸上画一个5x5的例子就会发现其实每一圈都是相同的，从左上角开始顺时针转一圈，因此该问题可以拆分成多个轮的循环，每一轮中都是先遍历上面的边，然后是右面的边，再从右到左遍历下面和从上到下遍历左边，其实二维下标还是不难写的，只要拿turn=0,1试验一下就好。真正搞心态的是最后那一轮的循环，因为最后剩的那一小点不是完整的遍历，具体来讲有两种可能：要么是横着的一行，要么是竖着的一列，这要取决于数组的长宽哪个大，所以循环多少轮也跟长宽有关，应该是短边/2次数。所以整体来看是先循环min(m,n)/2整次，然后再根据短边是否中间还剩了一条来判断是否还需要一行或是一竖的循环

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        res = []
        for turn in range(min(m, n)//2):
            for j in range(turn, n-turn):
                res.append(matrix[turn][j])

            for i in range(turn+1, m-turn):
                res.append(matrix[i][n-turn-1])

            for j in range(n-turn-2, turn-1, -1):
                res.append(matrix[m-turn-1][j])

            for i in range(m-turn-2, turn, -1):
                res.append(matrix[i][turn])

        if min(m, n)%2 == 1:
            turn = min(m, n)//2
            if m<=n:
                for j in range(turn, n-turn):
                    res.append(matrix[turn][j])
            else:
                for i in range(turn, m-turn):
                    res.append(matrix[i][n-turn-1])
        return res
# @lc code=end

