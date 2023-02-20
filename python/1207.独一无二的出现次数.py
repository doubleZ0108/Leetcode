#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#
# 解法1(T100% S32%)：如果题做多了这道题两行就能做完，首先调用Counter()统计每个元素出现的频次，然后将values()通过集合去重，判断去重之后的元素数量是否跟原来一致

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        if len(cnt) == len(set(cnt.values())):
            return True
        else:
            return False
# @lc code=end

