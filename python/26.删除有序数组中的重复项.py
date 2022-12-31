#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项
#
# 解法1：数组的inplace操作还是很有趣但也挺考逻辑的，基础想法就是如果我跟前一个数一样那就把我移动到最后面，让后面的依次往前一个
#    改进1(T18% S14%): 因为数组保证升序，所以一次可以把一串相同的都直接拿到后面，这就首先要往后搜索找到一直值相同的位置，然后计算一下gap，也就是后面的要往前挪多长。最难点是终止条件：如果一直找到数组结尾了都相同，那证明最后一个元素一直重复到结尾，可以终止了；或者如果找到不相同的元素比当前元素还小，也就意味着是之前串过的，也可以终止
# 
# 解法2(T97% S81%)：之前想的太复杂，其实很简单。双指针，j指针初始比i往后一位，如果ij指向的元素相等，则j往后移动，证明这个数结果中有了不需要继续保留；否则，i往后移一个位置，把这个位置填充上j指向的这个不相同元素。终止条件就是j指针出界，也就是说快指针把所有数都看完了。本质上i每次都是保存不同的值

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return len(nums)

        i, j = 0, 1
        while j<len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i+1

    def OtherSolution(self, nums):
        i = 0
        while i<len(nums):
            si = i
            while si < len(nums) and nums[si] == nums[i]: si += 1

            if si==len(nums) or nums[si]<nums[i]: return i+1

            if si == i+1:
                i += 1
                continue

            gap = si-i-1
            for k in range(si, len(nums)):
                nums[k-gap] = nums[k]
            
            i += 1

# @lc code=end

