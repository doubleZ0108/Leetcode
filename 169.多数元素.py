#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#
# 解法1(T38% S72%): 首先一次遍历用哈希表保存每个元素出现的次数，再遍历哈希表，如果次数大于n//2则返回key
# 
# ✨解法2(T92% S20%): 题目说要求$O(1)$空间复杂度，首先随便找一个数作为最多的数，并设置一个counter，一次遍历，如果当前元素等于设置的这个数则counter++，否则counter—，如果counter归零了，则再选取下一个数作为最多的数。思想的本质是如果某一个数比半数还多，即使其他所有人都来跟我一换一的杀，我还能剩下至少一个，何况其他人可能还互相杀，我能剩下的就更多了
#   但不懂为啥空间消耗反倒更大了

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 解法2
        major = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] == major:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    major = nums[i+1]
        return major


    def otherSolution(self, nums):
        # 解法1
        table = {}
        for num in nums:
            if num not in table: table[num] = 1
            else: table[num] += 1

        for k, v in table.items():
            if v > len(nums)//2: return k
# @lc code=end

