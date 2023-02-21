#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# 解法1：稍微一想，奇数位之和和偶数位之和的最大值肯定不是最优解，因为可能有一个超大户人家，不要轻易的偷它周围的那两个而是要看着它偷，所以可能出现连续两家都不偷
# 
# 解法2(超时)：深搜模拟所有可能的偷的结果，最终返回所有可能结果中的最大值
# 
# 解法3(T96% S30%)：动态规划，这个想法非常有趣，也是第一次见的动态规划形式。因为考虑到偷不偷当前的第i家跟之前的i-1家，i-2家，甚至i-3家有很大关系，有这样几种可能：1）偷第一家和第三家；2）偷第二家和第四家；3）偷第一家和第四家，这里最不好理解的的是3），但可以深入理解解法1提到的问题或者看这个小例子[2,1,1,2]。为什么说动态规划形式是第一次见呢，因为一般的动态规划都只有i-1和i的关系，但这里到四个人的关系，前三个人存不存在都不一定，所以代码层面可以把之前简单的max()函数替换成三条if和>的连续判断。这题整体还是非常有趣的

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            thismax = nums[i]
            if i-1>=0 and nums[i-1]>thismax:
                thismax = nums[i-1]
            if i-2>=0 and nums[i-2]+nums[i]>thismax:
                thismax = nums[i-2]+nums[i]
            if i-3>=0 and nums[i-3]+nums[i]>thismax:
                thismax = nums[i-3]+nums[i]

            # nums[i] = max(nums[i-1], nums[i-2]+nums[i], nums[i-3]+nums[i])
            nums[i] = thismax
        return max(nums)
    
    # 解法2 超时
    def rob2(self, nums: List[int]) -> int:
        res = []
        def deepin(i, pre, cnt):
            if i>=len(nums):
                res.append(cnt)
                return
            if not pre:
                deepin(i+1, True, cnt+nums[i])
            deepin(i+1, False, cnt)
        
        deepin(0, False, 0)
        deepin(0, True, 0)
        return max(res)
# @lc code=end

