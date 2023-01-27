#
# @lc app=leetcode.cn id=1154 lang=python
#
# [2309] 兼具大小写的最好英文字母
# 
# 解法1(T100% S28%)：首先将字符串中所有不同的字母都存入集合或哈希表中（可以通过Counter()库，也可以直接用set()），然后从第26个字母往前遍历，如果这个字母的大小写都在哈小表中则直接返回即可，它是最好字母且一定是最大的那个
#    python中`lower()`, `upper()`将字符串转为大小写


# @lc code=start
class Solution:
    def greatestLetter(self, s: str) -> str:
        # cnt = Counter([_ for _ in s]).keys()
        cnt = set([_ for _ in s])
        for i in range(26, 0, -1):
            alpha = chr(i+ord('a')-1)
            if alpha.lower() in cnt and alpha.upper() in cnt:
                return alpha.upper()
        return ""
# @lc code=end