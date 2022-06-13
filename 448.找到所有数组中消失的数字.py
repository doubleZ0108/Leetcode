#
# @lc app=leetcode.cn id=448 lang=python
#
# [448] 找到所有数组中消失的数字
#
"""
解法1(T98% S86%): 开辟一个n长度的标志位数组，首先一次遍历nums数组，将存在的元素标志为True，再一次遍历标志位数组，将False位对应的下标加入结果数组中，它们就是消失的数

解法2(T8% S46%): 排序，然后双指针分别指向nums和1～n的数，判断1～n的每个数字是否在已有序的数组nums中：如果数字比nums下标小，则代表nums中没有这个数，则加入结果中；如果数字等于nums中对应的数则指针都后移；否则nums下标移动一位，最后再将数字指针一直往后移动到数组长度将后面一截消失的数加入数组中

解法3(T72% S13%): 集合，`set(1~n) - set(nums)`的结果就是消失的数，差集可以用库函数`difference()`，注意结果需要转换为list输出（但不需要再排序，set会默认按照数字大小排序）

✨解法4(T30% S44%): 不开辟新空间且时间$O(N)$，遍历原数组，将每个数字对应下标的位置内容变为对应的负数，最后再一次遍历，找到仍为正数的，它们就是消失的数
"""

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        res = []
        for i in range(len(nums)):
            if nums[i] > 0: res.append(i+1)
        return res

    def otherSolution(self, nums):
        # 解法3
        return list(set(i for i in range(1, len(nums)+1)).difference(set(nums)))

        # 解法1
        bitmap = [False for _ in range(len(nums)+1)]
        for num in nums:
            bitmap[num] = True
        res = []
        for i in range(1, len(bitmap)):
            if not bitmap[i]: res.append(i)
        return res

        # 解法2
        nums.sort()
        i, j = 0, 1
        res = []
        while i<len(nums) and j<=len(nums):
            if j<nums[i]: 
                res.append(j)
                j += 1
            elif j==nums[i]:
                i += 1
                j += 1
            else:
                i += 1
        while j<=len(nums): 
            res.append(j)
            j += 1
        return res

Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
# @lc code=end

