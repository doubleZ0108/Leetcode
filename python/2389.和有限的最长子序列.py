#
# @lc app=leetcode.cn id=2383 lang=python
#
# [2389] 和有限的最长子序列
#
# 解法1(T5% S5%)：把问题想得稍微有点复杂，但也能解，我们使用一个有序的滑动窗口来维护，对于每个query，从头到尾遍历所有nums，如果当前num>query那它肯定放不进滑窗；如果当前滑窗内总和+num≤query，那肯定可以把这个num先放进来；如果num小于当前滑窗内的最大值那就贪心的把滑窗内的最大值弹出并加入这个最小值。最终滑窗内剩下的元素就是最长的子序列
#
# 解法2(T12% S5%)：因为只是子数组，没说连续子数组，而且刚才的滑窗也不是内部按下标顺序的，因此nums的顺序不重要，那不妨先对nums排个序，这样从头开始求和肯定是最小的，加到哪超过了query就停
#   改进：还有很多改进空间，比如先让queries保留原顺序的排序，这样只需要一次遍历nums的前缀和即可

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    # 解法1
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = [0 for _ in range(len(queries))]
        for i, query in enumerate(queries):
            win = SortedList()
            total = 0
            for num in nums:
                if num > query: continue
                if total + num <= query:
                    total += num
                    win.add(num)
                elif win and num < win[-1]:
                    total -= win.pop()
                    total += num
                    win.add(num)
            res[i] = len(win)
        return res
    
    # 解法2
    def answerQueries2(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        for query in queries:
            total = 0
            for i, num in enumerate(nums):
                total += num
                if total > query:
                    res.append(i)
                    break
                if i == len(nums)-1:
                    res.append(len(nums))
            
        return res
# @lc code=end