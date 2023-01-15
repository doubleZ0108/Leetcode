#
# @lc app=leetcode.cn id=2293 lang=python3
#
# [2293] 极大极小游戏
#

# @lc code=start
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newNums = [0 for _ in range(len(nums)//2)]
            for i in range(len(newNums)):
                if i%2:
                    newNums[i] = max(nums[2*i], nums[2*i+1])
                else:
                    newNums[i] = min(nums[2*i], nums[2*i+1])
            nums = newNums
        return nums[0]
# @lc code=end

