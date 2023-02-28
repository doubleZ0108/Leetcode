#
# @lc app=leetcode.cn id=1154 lang=python
#
# [2363] 合并相似的物品
#
# 解法1(T70% S16%)：因为两个集合中物体都是唯一的，因此只需要先对两个集合排序，然后通过双指针将二者相同的物品重量合并即可，类似于两个有序链表的合并，先ij一起循环，再各自循环到末尾即可

# @lc code=start
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.sort(key=lambda x: x[0])
        items2.sort(key=lambda x: x[0])

        res = []
        i, j = 0, 0
        while i<len(items1) and j<len(items2):
            if items1[i][0] == items2[j][0]:
                res.append([items1[i][0], items1[i][1]+items2[j][1]])
                i += 1
                j += 1
            elif items1[i][0] < items2[j][0]:
                res.append(items1[i])
                i += 1
            else:
                res.append(items2[j])
                j += 1
        while i<len(items1):
            res.append(items1[i])
            i += 1
        while j<len(items2):
            res.append(items2[j])
            j += 1
        return res
# @lc code=end