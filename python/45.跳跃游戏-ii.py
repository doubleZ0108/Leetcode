#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# 解法1：广度优先搜索，通过队列来维护，每次从队列中弹出头节点，根据该节点能往后跳跃的最大长度依次将他们加入后续队列，并设置跳跃数+1，这样，当遇到第一个能跳到结束为止的就返回
#     改进1：如果超过数组长度的就不用加入队列了
#     改进2(超时 82/109)：从这点能跳的最远处往前遍历，这样可以更快收敛
#
# ✨解法2(T82% S84%)：贪心，自己是真的不擅长贪心，因为站在i可以往后跳0～nums[i]步，因此只要i+nums[i]能超过数组长度那就可以用最少的次数跳跃，因此我对所有我能跳的这nums[i]步每个位置都计算j+nums[j]，通过贪心的想法选，但有个提前终止，如果我自己这次就能直接跳过去那就再跳1次就好了

# @lc code=start
class Solution:
    # 解法2
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        i = 0
        res = 0
        while i<len(nums)-1:
            rightmost, ridx = i, i
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                if j == len(nums)-1:
                    return res+1
                if j+nums[j] >= rightmost:
                    rightmost = j+nums[j]
                    ridx = j
            i = ridx
            res += 1
        return res
    
    # 解法1 超时
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        queue = [(0, 0)]
        while queue:
            idx, cnt = queue.pop(0)
            if idx == len(nums)-1:
                return cnt
            for i in range(min(len(nums)-1, idx+nums[idx]), idx, -1):
                queue.append((i, cnt+1))
# @lc code=end

