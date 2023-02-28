#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#
# 解法1(T74% S12%)：Python处理这种二进制直接通过bin()无论啥有没有符号的整数都被转成二进制字符串了，再统计有多少字符1即可

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter(bin(n)[2:])['1']
        
# @lc code=end

