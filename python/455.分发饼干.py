#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#
# 解法1(T86% S40%)：双指针。首先把两个数组排序，两个指针分别指向两个数组，如果这位的饼干不够，则饼干往后移一位；如果够，则两个指针都后移一位。最后返回指向小朋友胃口的指针位置。

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(g)==0 or len(s)==0: return 0

        g.sort()
        s.sort()

        i, j = 0, 0
        while i<len(g) and j<len(s):
            if s[j]<g[i]:
                j += 1
                continue
            else:
                i += 1
                j += 1
        
        return i

# @lc code=end

