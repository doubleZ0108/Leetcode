#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:][::-1]
        bits += "0"*(32-len(bits))
        return int(bits, 2)
        
# @lc code=end

