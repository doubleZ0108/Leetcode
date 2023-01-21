#
# @lc app=leetcode.cn id=1824 lang=python3
#
# [1824] 最少侧跳次数
#
# 解法1(T73% S62%)：题目看起来挺长挺唬人，但仔细分析贪心的来做就可以，不需要很复杂的dp或是其他，初始我们站在2，如果一路上没有石头就放心大胆的往前走不需要任何操作，如果发现前面i+1是石头，那就要分两种情况，比如我当前在跑道二：1）如果正前面i+1是石头，并且当前跑道一也是石头，那我没得选只能侧跳到跑道三；2）否则，我可以看看下一个我可能会碰到的石头在哪条跑道上，我可以贪心的把它也给跳过，直接跳到一条很久都不会遇到石头的路上，但要注意，石头可能在一条跑道上相邻，记得把跟i+1重复的跳过。因为只有三条跑道，可以直接写if-else来跳过，也可以通过集合set的减法来做

# @lc code=start
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        where = 2
        res = 0
        for i in range(0, len(obstacles)-1):
            if obstacles[i+1]==where:
                res += 1
                s = set([1,2,3]) - set([obstacles[i+1]])

                if obstacles[i]!=0:
                    s -= set([obstacles[i]])
                else:
                    for j in range(i+2, len(obstacles)):
                        if obstacles[j]!=0 and obstacles[j]!=obstacles[i+1]:
                            s -= set([obstacles[j]])
                            break
                where = list(s)[0]
        return res
# @lc code=end

