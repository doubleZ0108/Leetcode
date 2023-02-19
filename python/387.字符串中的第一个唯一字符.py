#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# 解法1(T81% S85%)：题目是很好想到解法的，但核心是判断一个字母是否出现两次还是要涉及到查找，那还不如干脆直接上来就用哈希表对每个字符的出现频次做个统计呢，这点复杂度在算法题里一般都不算个事


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for idx, ch in enumerate(s):
            if cnt[ch] == 1:
                return idx
        return -1
# @lc code=end

