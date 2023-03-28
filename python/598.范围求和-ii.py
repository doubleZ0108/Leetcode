#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#
# 解法1(超时)：按照题干描述进行模拟，三重循环根据ops让对应位置加1
#
# 解法2(T33% S14%)：仔细一想，由于最终只是要找最大值的数量，全模拟一遍属实是浪费了，最终最大的值取决于什么呢？取决于ops里最小的横竖范围划定的区域，因此只需要找ops里的最大值和最小值，他们的面积就是最终最大值的数量。如果ops==0，则返回的是m*n而不是0

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0: return m*n
        return min([x[0] for x in ops]) * min([x[1] for x in ops])
# @lc code=end

