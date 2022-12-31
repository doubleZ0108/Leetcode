#
# @lc app=leetcode.cn id=134 lang=python
#
# [134] 加油站
#
"""
解法1(超时)：基础想法很简单，依次把每个点作为起点进行遍历，判断是否能完整的走一圈
    改进1(T6% S95%)：基础想法的缺点也很明显，每个节点都作为起点走一圈显然做了很多无用功。比如有100个站点，如果从0→40都没问题，但41油不够，那很显然从1从2从3出发到41还是会被卡住（因为既然能从0出发它的油肯定够走到这些站），所以接下来我可以直接从42开始遍历（遍历的方法就是基础的解法1），如果能恰好走一圈则就返回42，如果在哪卡住了就再直接跳过中间那些站，而如果把100个站都跳过了，就也可以放心的说所有站开始都不能完整走一圈

解法2(T71% S69%)：一重循环。还是改进1的想法不过更统一的实现，设定两个变量run和rest，它们都是每步剩余油量的累计，但当走到某步发现剩余油为负了，则清空run，并把其实位置设为当前位置+1，而rest始终一直累积。最终把每个加油站都看完了后如果rest是负的就证明走不完，否则start指向的位置就可以成功走一圈
"""

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 解法2
        rest, run, start = 0, 0, 0
        for i in range(len(gas)):
            run += (gas[i] - cost[i])
            rest += (gas[i] - cost[i])

            if run < 0:
                start = i + 1
                run = 0
        return -1 if rest < 0 else start

        
    def otherSolution(self, gas, cost):
        # 解法1
        i = 0
        while i < len(gas):
            j = i
            remain = 0
            count = 0
            while count < len(gas):
                remain += (gas[j] - cost[j])
                if remain < 0: break
                j = (j + 1) % len(gas)
                count += 1
            if count == len(gas): return i
            else: i += count if count > 0 else 1

        return -1
# @lc code=end

