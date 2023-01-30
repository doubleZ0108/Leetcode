#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#
# 解法1(T35% S82%)：还是一样采用log来做，首先如果是0和负数直接False，然后计算n对3的log并去整，再计算3的幂次能否恢复这个数；需要注意的是，取整要用round()不能用下取整int()，否则例如243这种数会计算得4.99999产生误差精度

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0: return False

        return math.pow(3, round(math.log(n, 3))) == n
# @lc code=end

