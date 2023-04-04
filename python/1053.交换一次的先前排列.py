#
# @lc app=leetcode.cn id=1053 lang=python
#
# [1053] 交换一次的先前排列
#
# 解法1(解答错误 44/52)：看到几个示例的规律，从后往前找第一组(i, j)对，满足arr[i]>arr[j]，交换他们
# 解法2(T46% S42%)：整体思想跟我是差不多的，区别在于更理论化的探讨i和j的选取方式，大致代码差不多，但差的是细节

# @lc code=start
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1]:
                j = len(arr)-1
                while arr[j]>=arr[i] or arr[j]==arr[j-1]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                break
        return arr
# @lc code=end

