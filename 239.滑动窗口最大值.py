#
# @lc app=leetcode.cn id=239 lang=python
#
# [239] 滑动窗口最大值
#
# 本质上相当于对一个一维图像求nn.MaxPool1d

# 解法1(超时): 两重for循环，每次找到当前k个数里的最大值
# 
# 解法2(超时 不过比解法1多过了cases): 直观想到某一个最大值很可能是附近小区间的局部最大值，可以试探的往前走，看看我这个最大值能一直维护地位到哪
#   改进：不只维护一个数，而是需要一个辅助数据结构存储每个数能通知的区域（但时间过于复杂想想）
#   另一种解释是，如果新进来一个很大的数，那之前所有很小的东西都没用了
# 
# 解法3(T30% S65%)：单调队列。维护一个窗口长度的单调队列，存的值是下标而不是值本身。每往后走一步，如果当前队头的下标出界了就把它丢掉（国王年老死了），新来的人只要能力够强就不停的把队列里把它小的踢出掉，直到找到他也打不过的待下，最后每次只需把队列首元素作为当前窗口的最大值即可

# @lc code=start
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1: return nums

        res, win = [], []
        for i in range(len(nums)):
            if i>=k and win[0]<i-k+1:
                win.pop(0)
            while win and nums[win[-1]]<nums[i]:
                win.pop(-1)
            win.append(i)
            if i>k-2:
                res.append(nums[win[0]])
        return res

    def otherSolution(self, nums, k):
        # 解法2(超时)
        nowmax, nowmax_index = nums[0], 0
        for i in range(k):
            if nums[i] > nowmax:
                nowmax, nowmax_index = nums[i], i

        ans = [nowmax]

        for i in range(k, len(nums)):
            if i-nowmax_index < k:     
                if nums[i] >= nowmax:
                    nowmax, nowmax_index = nums[i], i
                    ans.append(nums[i])
                else:
                    ans.append(nowmax)
            else:   # 之前最大的已经出窗了
                nowmax, nowmax_index = nums[i], i
                for j in range(i-k+1, i+1):
                    if nums[j] > nowmax:
                        nowmax, nowmax_index = nums[j], j
                ans.append(nowmax)
        return ans

        # 解法1(超时)
        ans = []
        for i in range(len(nums)-k+1):
            thismax = nums[i]
            for j in range(i+1, i+k):
                if nums[j] > thismax:
                    thismax = nums[j]
            ans.append(thismax)
        return ans

Solution().maxSlidingWindow([1,3,1,2,0,5], 3)
# @lc code=end

