#
# @lc app=leetcode.cn id=392 lang=python
#
# [392] 判断子序列
#
# 解法1(T85% S77%): 遍历s的每个字符，用一个指针指向t，s的每个字符在t里顺序的找，如果一直没找到那后面也不用看了，肯定False了；找到一个字符后，下次直接在后面接着找就好了

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        for l in s:
            while i < len(t):
                if t[i] == l:
                    break
                i += 1
            i += 1
            if i > len(t):
                return False
        return True
# @lc code=end

