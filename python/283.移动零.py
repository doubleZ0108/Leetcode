#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# 解法1(T5% S34%)：思想很简单但代码还是很长很复杂的，外层遍历，如果找到0则不断试探跟他相连的所有0，共cnt个，将后面的元素直接跳过cnt位向前覆盖；同时维护了全局的sum标识右侧总共有多少元素应该为0了，元素向前覆盖可以少看这么多，最终再将后面sum个元素都置为0
# 
# 解法2(T80% S47%)：不要想着只遇到0才移动，因为最终0总归是要浮动到右侧的，而且不能打乱原来的顺序，因此应该像冒泡排序一样，一点一点动。具体而言，左右指针初始时都指向0，右指针不断试探，找到非零元素就将当前两指针元素交换，并且左指针右移。本质相当于一点点把非零的元素移动到左边

# @lc code=start
class Solution:
    # 解法2
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

    # 解法1
    def moveZeroes1(self, nums: List[int]) -> None:
        i = 0
        sum_ = 0
        while i<len(nums)-sum_:
            if nums[i]!=0:
                i += 1
                continue
            
            cnt = 1
            k = i
            k += 1
            while k<len(nums) and nums[k]==0:
                k += 1
                cnt += 1    

            j = k
            while j<len(nums)-sum_:
                nums[j-cnt] = nums[j]
                j += 1

            sum_ += cnt
            i += 1

        while i<len(nums):
            nums[i] = 0
            i += 1
# @lc code=end

