#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# 解法1(T72% S77%)：互为异位词等同于排序后字符串相同，因此通过哈希表来维护，key设为排序后的字符串，val来保存每个异位词结果，最后返回哈希表值的集合即可

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for s in strs:
            s_ = "".join(sorted(s))
            if s_ not in table:
                table[s_] = [s]
            else:
                table[s_].append(s)
        return list(table.values())
# @lc code=end

