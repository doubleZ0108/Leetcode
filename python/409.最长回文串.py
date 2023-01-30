#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# 解法1(T54% S23%)：不要想的太复杂，首先统计每个字母出现的频次，如果是偶数个那他们放在两边肯定能对称，如果是奇数个有两种可能：1）放在正中间可以对称，2）删掉一个也就变成了偶数个。因此统计完之后，把第一个奇数放在中间，剩下的所有奇数都减去1

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter([_ for _ in s]).values()
        res = 0
        flag = False
        for cnt in count:
            if cnt%2==0:
                res += cnt
            else:
                if not flag:
                    flag = True
                    res += cnt
                else:
                    res += cnt-1
        return res
# @lc code=end

