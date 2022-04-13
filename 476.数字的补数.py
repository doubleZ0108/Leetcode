#
# @lc app=leetcode.cn id=476 lang=python
#
# [476] 数字的补数
#
# 解法1(T38% S13%):  标准的除2取余法想把原数变为二进制，并用数组保存每一位，再依次构建补数的十进制
#   改进1(T96% S81%): 取消数组，依次循环边拆边建
#   改进2: 可进一步把`//= 2`变为右移`>> 1` ，`*= 2`变为左移`<< 1`
#       注意移位运算移动一位就相当于乘除2了！
# 
# 解法2(T75% S22%): 通过python库函数
#   `bin()`：十进制 → 二进制
#   `int("0bxxx", r)`：r进制 → 十进制


# @lc code=start
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 解法1 改进
        res = 0
        rank = 1
        while num>1:
            bi = num % 2
            num >>=  1
            res += rank if bi==0 else 0
            rank <<= 1
        
        return res

    def otherSolution(self, num):
        # 解法2
        # `bin(num)[2:]`计算二进制（字符串，且以0b开头因此要去掉）
        # `map()`将每个字符变为数字然后去非，再转换为数字，并最后转换为字符（否则没法拼接）
        # `“”.join()`对二进制数组拼接
        # `int(””, 2)`将二进制转为十进制
        return int("".join(map(lambda x: str(int(not int(x))), bin(num)[2:])), 2)


        # 解法1
        bi_arr = []
        while num>1:
            bi_arr.append(num % 2)
            num //= 2
        
        res = 0
        for i, bi in enumerate(bi_arr):
            res += 2**i if bi==0 else 0
        return res
# @lc code=end

