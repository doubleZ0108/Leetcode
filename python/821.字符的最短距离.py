#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#
# 解法1(T33% S99%)：因为是简单题，直接两重循环做不会有大问题，不过这道题对于边界条件的判断还是不错的。站在一个位置如果已经是c了那这位结果肯定是最小的0了，如果不是则往左找到第一个c的位置以及往右找第一个c的位置选最小的距离。需要注意当j下标已经越界了就不用看了，由于Python独特的语法，即使j=-1也不会报错而是选最后一位，然而最后一位可能等于c，所以要特别注意下标越界的情况

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [-1 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == c:
                res[i] = 0
            else:
                j = i-1
                while j>-1 and s[j]!=c:
                    j -= 1
                if j>-1 and s[j] == c:
                    res[i] = abs(i-j)

                j = i+1
                while j<len(s) and s[j]!=c:
                    j += 1
                if j<len(s) and s[j] == c:
                    res[i] = abs(i-j) if res[i]==-1 else min(res[i], abs(i-j))
                
        return res
# @lc code=end

