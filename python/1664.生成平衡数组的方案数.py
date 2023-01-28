#
# @lc app=leetcode.cn id=1664 lang=python3
#
# [1664] 生成平衡数组的方案数
#
# 解法1(超时 71/105)：维护删除元素左边的奇偶分别之和，依次循环每个位置，重新计算右面的奇偶之和，本质相当于优化了的两重暴力循环
#     改进1(T68% S76%)：解法1的问题也很明显，我们应该把右面的总和也维护起来，每次重复计算太慢了，首先一次循环将数组全部的奇偶总和统计起来；循环每个删除的位置时，让对应的维护变量减去当前值（因为当前值被删了），然后交换右侧两维护变量的值（因为删了一个元素，后面所有下标都变位了），因为左边的奇偶之和也都维护了，所以计算下总和就好，计算完要把右侧的两变量再交换回去，因为下一个删除位置奇偶又会交替了

# @lc code=start
class Solution:
    # 改进1
    def waysToMakeFair(self, nums: List[int]) -> int:
        leftsum0, leftsum1 = 0, 0
        rightsum0, rightsum1 = 0, 0
        for i, num in enumerate(nums):
            if i%2==0:
                rightsum0 += num
            else:
                rightsum1 += num
                
        res = 0
        for i, num in enumerate(nums):
            if i%2==0:
                rightsum0 -= num
            else:
                rightsum1 -= num
            rightsum0, rightsum1 = rightsum1, rightsum0

            if leftsum0+rightsum0 == leftsum1+rightsum1:
                res += 1
            
            if i%2==0:
                leftsum0 += num
            else:
                leftsum1 += num
            rightsum0, rightsum1 = rightsum1, rightsum0
        return res

    # 解法1 超时
    def waysToMakeFair1(self, nums: List[int]) -> int:
        leftsum0, leftsum1 = 0, 0
        res = 0
        for i in range(len(nums)):
            rightsum0, rightsum1 = 0, 0
            for j in range(i+1, len(nums)):
                if (j-1)%2==0:
                    rightsum0 += nums[j]
                else:
                    rightsum1 += nums[j]

            if leftsum0+rightsum0 == leftsum1+rightsum1:
                res += 1
                
            if i%2==0:
                leftsum0 += nums[i]
            else:
                leftsum1 += nums[i]
        return res
# @lc code=end

