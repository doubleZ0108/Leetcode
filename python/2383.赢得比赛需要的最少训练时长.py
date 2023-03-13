#
# @lc app=leetcode.cn id=2383 lang=python
#
# [2383] 赢得比赛需要的最少训练时常
#
# 解法1(T97% S68%)：精力和经验完全可以分成两部分看，首先是Energy比较好理解，每次都往下扣，因此我的初始经验要比全部需要的energy还大1，所以只需要对energy求和就好，但别忘了如果我初始精力就很大那就不需要训练精力了；经验稍复杂一点，当我遇到一个新的怪时，如果我当前经验比他大，那直接KO，我增加他的经验，如果我比他小，那就需要初期多训练这个差值，让结果变量增加这么多，但同样要注意此时我也会击杀他，因此还要多加上这些经验

# @lc code=start
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res_en = sum(energy) - initialEnergy + 1
        if res_en < 0: res_en = 0
        res_ex = 0
        myexp = initialExperience + res_ex
        for exp in experience:
            if myexp > exp:
                myexp += exp
            else:
                res_ex += exp - myexp + 1
                myexp += exp - myexp + 1 + exp
        return res_en + res_ex

# @lc code=end