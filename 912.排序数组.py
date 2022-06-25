#
# @lc app=leetcode.cn id=912 lang=python
#
# [912] 排序数组
#
"""
解法1(超时)：冒泡排序，两重循环，外层控制走多少轮（len-1次就可以了，最后一个元素会自然有序），内层从0～len-i-1一次遍历，每次将相邻的元素中更小的浮动到右边，内层每走完一整轮，后面就多了一个有序的元素
    改进1(超时): 如果内层在一轮中一次都没交换过，则代表数组已经有序，可以提前终止

解法2(超时)：选择排序，两重循环，外层跟冒泡一样，内层每次从i～len找当前剩余最小的数，把它直接交换到第i个位置，那就是它的最终位置

解法3(超时)：插入排序，两重循环，外层从1～len，内层while循环从i～0，将比当前元素大的数一个一个往后挪，然后把当前数插入到之前序列中合适的位置

解法4(T42% S75%)：归并排序，从中间划分数组，然后分别先递归的排序左边和右边，再合并有序数组，递归终止条件是数组中只有一个数

解法5(T68% S93%)：快速排序，首先选择一个数作为pivot（不妨选第一个数），不断把所有比它小的都放在它左边，比它大的都放它右边，然后分别递归数组左侧和右侧
    快排对于原本就基本有序的序列效果很差，可以先打乱一下`random.shuffle(nums)`

"""
import random

# @lc code=start
class Solution(object):
    def partition(self, nums, first, last):
        pivot = nums[first]
        left, right = first+1, last
        while left <= right:
            while left<=right and nums[left]<=pivot:
                left += 1
            while left<=right and nums[right]>=pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[first], nums[right] = nums[right], nums[first]
        return right

    def sortArray_(self, nums, first, last):
        if first < last:
            splitpos = self.partition(nums, first, last)
            self.sortArray_(nums, first, splitpos-1)
            self.sortArray_(nums, splitpos+1, last)
        return nums

    def sortArray(self, nums):
        random.shuffle(nums)
        return self.sortArray_(nums, 0, len(nums)-1)


    def quickSort(self, nums, i, j):
        if i>j: return

        low, high = i, j
        pivot = nums[low]

        while i<j:
            while i<j and nums[j]>=pivot: j -= 1
            if nums[j] < pivot:
                nums[i] = nums[j]
                i += 1
            while i<j and nums[i]<=pivot: i += 1
            if nums[i] > pivot:
                nums[j] = nums[i]
                j -= 1
        nums[i] = pivot
        self.quickSort(nums, low, i-1)
        self.quickSort(nums, i+1, high)

        return nums

    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            leftArr = self.mergeSort(nums[:mid])
            rightArr = self.mergeSort(nums[mid:])

            i, j, k = 0, 0, 0
            while i<len(leftArr) and j<len(rightArr):
                if leftArr[i] < rightArr[j]:
                    nums[k] = leftArr[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = rightArr[j]
                    j += 1
                    k += 1
            while i<len(leftArr):
                nums[k] = leftArr[i]
                i += 1
                k += 1
            while j<len(rightArr):
                nums[k] = rightArr[j]
                j += 1
                k += 1
        return nums

    def bubbleSort(self, nums):
        flag = False
        for i in range(len(nums)-1):
            flag = False
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = True
            if not flag: break
        return nums

    def selectSort(self, nums):
        for i in range(len(nums)-1):
            minVal, minIdx = nums[i], i
            for j in range(i, len(nums)):
                if nums[j] < minVal:
                    minVal = nums[j]
                    minIdx = j
            if minIdx != i:
                nums[i], nums[minIdx] = nums[minIdx], nums[i]
        return nums

    def insertSort(self, nums):
        for i in range(1, len(nums)):
            tmp = nums[i]
            j = i
            while j>0 and nums[j-1]>tmp:
                nums[j] = nums[j-1]
                j -= 1
            if j != i:
                nums[j] = tmp
        return nums

Solution().sortArray([2,3,5,1])
# @lc code=end

