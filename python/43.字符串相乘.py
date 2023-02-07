#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# 解法1(T28% S77%)：第一次做大数乘法，才意识到好久没有扒拉手指头数数了，本质相当于num2的每一位去乘num1，然后再根据第几位乘以10的幂次，最后求和
#   按理说最后的求和也应该直接用字符串做，但字符串加法已经做过了就当已经写完了

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        multis = []
        for b in num2:
            bonus = 0
            tmp = ""
            for a in num1:
                tmp += str((int(a)*int(b)+bonus) % 10)
                bonus = (int(a)*int(b)+bonus) // 10
            if bonus > 0:
                tmp += str(bonus)
            multis.append(int(tmp[::-1]))
        
        res = 0
        for idx, num in enumerate(multis):
            res += num * 10**idx
        return str(res)
# @lc code=end

