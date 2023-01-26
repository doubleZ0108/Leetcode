#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# 解法1(T96% S54%)：题不难，本质上是10进制 → 26进制，但由于没有0这个数（而是Z=26这个数）所以代码写起来有点烦。还是循环num直到其归零，如果当前数不能整除26，那跟之前的进制转换是一样的，取余获得最后一位，再除以进率进行下一次循环；麻烦的是如果当前数整除26，则这位一定是Z，除了整除26之外还要递减1，把这个26往前串一下；最终再把结果反过来
#     10进制 → r进制：除r取余 倒过来

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            if columnNumber % 26 == 0:
                res += 'Z'
                columnNumber //= 26
                columnNumber -= 1
            else:
                res += chr(columnNumber%26 + ord('A') - 1)
                columnNumber //= 26
        return res[::-1]
# @lc code=end

