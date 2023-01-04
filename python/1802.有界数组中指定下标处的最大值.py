#
# @lc app=leetcode.cn id=1802 lang=python3
#
# [1802] 有界数组中指定下标处的最大值
#

# @lc code=start
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        i, j = 1, maxSum-n+1

        while i<=j:
            mid = (i+j)//2

            val = self.fastcal(mid, n, index)

            if val == maxSum:
                return mid
            elif val < maxSum:
                i = mid + 1
            else:
                j = mid - 1
        return j

    def cal(self, mid, n, index):
        val = mid
        this = mid
        for i in range(index-1, -1, -1):
            if this > 1:
                this -= 1
            val += this
        this = mid
        for i in range(index+1, n, 1):
            if this > 1:
                this -= 1
            val += this
        return val

    def fastcal(self, mid, n, index):
        val = mid
        if mid >= index + 1:
            val += ((mid - 1 + mid - index) * index) / 2
        else:
            val += 1 * (index + 1 - mid) + mid*(mid-1)/2
        
        if mid >= n - index:
            val += ((mid+mid-n+index) * (n-index-1)) / 2
        else:
            val += 1 * (n-mid-index) + mid * (mid-1)/2
        return val
        

# @lc code=end

