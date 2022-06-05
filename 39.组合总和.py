#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#
"""
解法1(T57% S34%)：整体跟零钱兑换有点像，大框架应该是一个递归的策略，不同点在于零钱兑换只需要求最后的一个总数，不需要保存硬币的组成，因此这里的递归函数肯定有一个参数是数组保存着可以达到组合的各个元素，递归的终止条件也就比较清晰，当剩余的数为0时，就可以将这个数组参数加到结果数组中了。那递归的参数都是什么呢？很自然肯定有一个数组`thepass`用于保存一种组合的所有组成，还应该有一个`target`数作为剩余数字。这两个就够了吗？因为每个数字可以不用或用多次，还应该有一个`idx`标识当前用的数字是哪个。剩下的核心问题就是如何构建递归内部的逻辑，还是考虑到每个数字都可以不用或用多次，因此递归的转移应该有两条路：
    1. 不用当前数：thepass不变，target保持不变，idx+1，直接递归
    2. 用当前数/再用一遍当前数：thepass加入当前数，target-当前数，idx不变，进行递归，这个递归如果成功了就直接添加到结果数组中了，如果没成功返回就证明当前数不应该用，所以要再把当前数`pop()`出去

    注意：递归终止时将thepass加入结果数组中是要copy()，否则下次递归会清空结果，导致最终返回的是空数组

解法2(T22% S80%)：还是递归的整体框架，其实不用idx标识当前看的是第几位，直接循环所有数字进行遍历即可。不过需要注意直接每次循环所有数字结果很容易重复，比如[2,2,3],[2,3,2],[3,2,2]会记录好几遍，因此可以首先对原数组排序，然后在递归中每次只取不小于上一次取的元素的值，同样的如果不成功返回了也还是要把这轮取的数pop出去
"""

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def combine(target, thepass):
            if target<0: return
            if target == 0:
                res.append(thepass.copy())
                return
            for cand in candidates:
                if len(thepass)>0 and cand < thepass[-1]: continue
                thepass.append(cand)
                combine(target-cand, thepass)
                thepass.pop()
        
        candidates.sort()
        combine(target, [])
        return res

    def otherSolution(self, candidates, target):
        res = []

        def combine(target, thepass, idx):
            if target<0 or idx>=len(candidates): return
            if target == 0:
                res.append(thepass.copy())
                return
            combine(target, thepass, idx+1)
            if target - candidates[idx] >= 0:
                thepass.append(candidates[idx])
                combine(target-candidates[idx], thepass, idx)
                thepass.pop()
        
        combine(target, [], 0)
        return res

Solution().combinationSum([2,3,5], 8)
# @lc code=end

