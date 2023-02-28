#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#
# 解法1(T31% S67%)：先去除掉原字符串中的-并将字母转为大写，从后往前按照步长为k遍历，如果不是第一组则将k位长的切片添加到结果的头部并添加-，否则将第一段（可能没有k长度的）添加到结果的开头

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.split("-")).upper()
        res = ""
        for i in range(len(s)-1, -1, -k):
            if i-k >= 0:
                res = "-" + s[i-k+1:i+1] + res
            else:
                res = s[:i+1] + res
        return res

# @lc code=end

