#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
# 解法1(T88% S13%)：是道很有趣的小题，比较考验对Python语法和排序的理解，可以通过enumerate()或者zip()为原数组绑定一维原始下标，这样排序之后还可以获取到原始下标，排序后再调用enumerate()可以获取到名词，注意写清楚这几个的区别就好

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [None for _ in range(len(score))]
        for prize, oridata in enumerate(sorted(enumerate(score), key=lambda x: -x[1])):
            idx, _ = oridata
            if prize == 0:
                res[idx] = "Gold Medal"
            elif prize == 1:
                res[idx] = "Silver Medal"
            elif prize == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(prize+1)
        return res
# @lc code=end

