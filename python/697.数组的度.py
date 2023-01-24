#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
# 解法1(T5% S70%)：首先我们先要知道数组的度为多少，先通过哈希表统计每个元素出现的频次，最高的频次就是度，但最大频次对应的元素可能有好几个，要把他们都存下来，因为最终结果要最小值。然后通过双指针分别指向开头结尾，最短连续数组肯定是要包含所有的最大频次元素，因此从左找到第一个最大频次元素，从右也找到第一个，此时左右指针的距离就是这个元素需要的最短连续子数组的长度，因为最大频次元素可能有好几个因此都要看一下

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = sorted(Counter(nums).items(), key=lambda x: x[1])
        freqs = []
        for i in range(len(cnt)-1, -1, -1):
            if cnt[i][1] == cnt[-1][1]:
                freqs.append(cnt[i][0])
            else:
                break

        minlength = len(nums)
        for freq in freqs:
            i, j = 0, len(nums)-1
            while i<j and nums[i]!=freq:
                i += 1
            while i<j and nums[j]!=freq:
                j -= 1
            minlength = min(minlength, j-i+1)
        return minlength
# @lc code=end

