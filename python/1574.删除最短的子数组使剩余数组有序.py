#
# @lc app=leetcode.cn id=1574 lang=python3
#
# [1574] 删除最短的子数组使剩余数组有序
#
# 解法1(T76% S10%)：删除一个子数组使得剩下的非递减，那无非是删最开头的一个子数组/删最后的一个子数组/删中间的一个数组，直观的来想肯定是删中间的一段会更好，那我们不妨先用两个指针i j分别从头从尾统计已经有序的部份，如果i≥j，就证明整个数组已经有序了提前返回；否则就类似下面这个例子，此时i～j中间的这些内容肯定是要背删掉的，除此之外还要删除左边的后半部份和右边的前半部份，那我们不妨再用两个指针l和r，l遍历前半段的每个元素，在后半段找arr[l]应该插入的位置，此时还要额外删除的就是r-j+i-l这些内容，那全局找最小值就可以了
#       1 2 3 10 4 2 3 5
#              i   j
#     <-    l ->   <- r  ->
#     
#     改进：因为涉及到频繁的查找，那不妨改进成二分查找

# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i, j = 0, len(arr)-1
        while i+1<len(arr)-1 and arr[i+1]>=arr[i]:
            i += 1
        while j-1>-1 and arr[j-1]<=arr[j]:
            j -= 1
        if i >= j:  # 原数组递增
            return 0

        base = j - i - 1
        res = min(len(arr)-i-1, j)
        for l in range(i, -1, -1):
            r = j
            while r<len(arr) and arr[r]<arr[l]:
                r += 1
            res = min(res, r-j+i-l+base)
        return res
# @lc code=end

