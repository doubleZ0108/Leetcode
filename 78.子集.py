#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#
"""
解法1(T73% S36%)：数字不同的子集总共应该有2^n-1个，由于测试样例不超过10，因此直接遍历输出这么多个就可以了。具体实现可以通过二进制串来做，例如原数组为[1,2,3]，二进制串首先初始化为000 代表所有数都不取；然后001 代表只取3；然后010 代表只取2；…；110代表取1和2。具体实现时可以直接通过`bin()`将十进制转换为二进制，同时不需要补前导0，直接将二进制串颠倒顺序然后依次将原数字放进来就好

解法2(T91% S20%)：标准的回溯 & 深搜题。dfs的参数包含一个当前位置cur和一个状态数组tmp，当cur指向原数组的最后一个位置就代表一条路已经完全走完了，此时就把状态数组复制一份加入结果中。那如何进行回溯呢？首先考虑把当前cur指向的元素加入结果中，递归下一位，如果合适则自然会加入到结果中，如果不合适则pop()出当前元素即不用当前元素，直接递归下一位
    改进1(T91% S90%)：暂存状态数组不需要作为参数一直传递，全局有一个就好
"""

# @lc code=start
import enum


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 解法2 改进1
        ans = []
        tmp = []

        def dfs(cur):
            if cur == len(nums):
                ans.append(tmp.copy())
                return
            tmp.append(nums[cur])
            dfs(cur+1)
            tmp.pop()
            dfs(cur+1)
        
        dfs(0)
        return ans


        

    def otherSolution(self, nums):
        # 解法1
        ans = []
        for i in range(2**len(nums)):
            bin_code = bin(i)[2:][::-1]
            buf = []
            for idx, bit in enumerate(bin_code):
                if bit == '1': buf.append(nums[idx])
            ans.append(buf)
        return ans

        # 解法2
        ans = []
        
        def dfs(cur, tmp):
            if cur == len(nums):
                ans.append(tmp)
            tmp.append(nums[cur])
            dfs(cur+1, tmp)
            tmp.pop()
            dfs(cur+1, tmp)
        
        dfs(0, [])
        return ans


Solution().subsets([1,2,3])
# @lc code=end

