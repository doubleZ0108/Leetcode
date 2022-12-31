#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#
# 解法1(T48% S50%)：直接利用python库函数转为10进制计算再转回2进制输出
#   `bin(xx)[2:]`：十进制数xx转二进制，结果为字符串，且以0b前导，因此要去掉
#   `int(a,2)`：二进制数a转十进制
# 
# 解法2(T48% S60%)：自己按照逻辑写（其实还有很多优化空间这里就不展开了），用两个指针分别指向字符串结尾（其实字符串反转逻辑更简单一点），然后不断计算两位的加和，然后取余数添加到结果字符串中，取除数作为进位，尾部能匹配上的串加完之后再把长的串自己计算一遍，最最后如果进位仍为1则结果再添加一个1

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 解法1
        return bin(int(a,2) + int(b,2))[2:]

    def OtherSolution(self, a, b):
        # 解法2
        if len(b) > len(a): a, b = b, a

        res = ""
        i = len(a)-1
        remain = 0
        for j in range(len(b)-1, -1, -1):
            this = int(a[i]) + int(b[j]) + remain
            remain = this // 2
            res = str(this % 2) + res
            i -= 1

        for i in range(i, -1, -1):
            this = int(a[i]) + remain
            remain = this // 2
            res = str(this % 2) + res
            
        if remain: res = "1" + res
        
        return res
        
# @lc code=end

