#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#
# 解法1(T11% S5%)：纯数组逻辑题。首先开辟一个足够大的二维空间，用题目中不会出现的字符填充，按照题干首先往下走(top→bottom)，然后斜着向上走(torighttop)，每走一步把一个字母放到对应的位置上，遇到上下边界就换方向，最终一次二维扫描组装最后的结果。唯一需要注意的是只有1行的时候要单独考虑，直接返回原字符串就好
#   改进1(T29% S14%)：空间状态压缩。注意到二维矩阵中有大量空间都是填充的垃圾值且之后输出时还要多判断一次，而且还不知道要开辟多少列，因此可以每行用一个链表来存结果，每走到新位置就在该行链表的结尾添加一个值
# 
# 解法2：其实可以有严格的数学对应关系，这里略

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 解法1 改进1
        if numRows == 1 or len(s)<=numRows: return s

        themap = [[] for _ in range(numRows)]
        i, j = 0, 0
        dir = "top->bottom"
        for idx in range(len(s)):
            themap[i].append(s[idx])
            if idx == len(s)-1: break

            if dir=="top->bottom":
                if i == numRows-1:
                    i -= 1
                    j += 1
                    dir = "torighttop"
                else:
                    i += 1
            elif dir=="torighttop":
                if i == 0:
                    i += 1
                    dir = "top->bottom"
                else:
                    i -= 1
                    j += 1

        res = ""
        for i in range(numRows):
            for k in range(len(themap[i])):
                res += themap[i][k]
        
        return res

    def otherSolution(self, s, numRows):
        # 解法1
        if numRows == 1 or len(s)<=numRows: return s

        themap = [['@']*len(s) for _ in range(numRows)]
        i, j = 0, 0
        dir = "top->bottom"
        for idx in range(len(s)):
            themap[i][j] = s[idx]
            if idx == len(s)-1: break

            if dir=="top->bottom":
                if i == numRows-1:
                    i -= 1
                    j += 1
                    dir = "torighttop"
                else:
                    i += 1
            elif dir=="torighttop":
                if i == 0:
                    i += 1
                    dir = "top->bottom"
                else:
                    i -= 1
                    j += 1

        res = ""
        for i in range(numRows):
            for k in range(j+1):
                if themap[i][k] != "@":
                    res += themap[i][k]
        
        return res

Solution().convert("PAYPALISHIRING", 3)
# @lc code=end

