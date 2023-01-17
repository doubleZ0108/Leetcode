#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#
# 解法1(T90% S80%)：总归是要一个一个数判断才能知道是否满足条件，通过取余和整除获取数字每一位即可，注意提中条件不能有0

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            flag = True
            tmp = i
            while tmp:
                if tmp % 10 == 0 or i % (tmp%10) != 0:
                    flag = False
                    break
                tmp //= 10
            if flag:
                res.append(i)
        return res
# @lc code=end

