#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#
# 解法1(T98% S88%)：这完全属于数学问题没见过了，与普通的10→2进制类似，也是除r取余倒着写，不过在于某次的余数可能是负数，因为最终结果肯定都是01字符串，因此加入结果时肯定要取abs()，但如果本来为负数，当前剩余n不是直接除r=-2，而是要n//-2 + 1

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        res = ""
        while n:
            remain = n % (-2)
            res += str(abs(remain))
            n = n//(-2) if remain>=0 else n//(-2)+1
        return res[::-1]
        
# @lc code=end

