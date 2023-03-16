#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# 解法1(T43% S76%)：没啥好说的，直接统计每个数二进制中1的个数就好，可以直接通过bin()[2:]将数字转为二进制，或者不断判断末尾对2取余的值，然后右移一位

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            # res.append(bin(i)[2:].count('1'))
            cnt = 0
            num = i
            while num:
                if num % 2 == 1:
                    cnt += 1
                num >>= 1
            res.append(cnt)
        return res
# @lc code=end

