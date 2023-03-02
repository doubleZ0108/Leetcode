#
# @lc app=leetcode.cn id=2357 lang=python
#
# [2357] 使数组中所有元素都等于零
#
# 解法1(T75% S17%)：看了题目的数据规模，放心大胆的循环，每轮操作都分为两步，首先一次循环找到最小的非零数，再依次循环让所有数都减去这个数，如果所有元素都已经为0了就可以结束了

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while True:
            minNum = 101
            for num in nums:
                if num != 0 and num < minNum:
                    minNum = num
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= minNum
            if minNum == 101:
                break
            cnt += 1
        return cnt
# @lc code=end