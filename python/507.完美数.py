#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#
# 解法1(T63% S95%)：不懂为啥这题是简单。。卡了我好一会，看一下题干都$10^8$了，直接一重循环肯定会超时的，循环到num/2也还是会爆炸。这题的脑筋急转弯在于如果d是num的因子，则num//d也一定是num的因子，相当于一次就能加两个，这样终止条件也缩到$d^2<num$，注意下num本身不能被统计就好
#
# 解法2：官方的解法2太…了，这么大的范围内在只有5个完全数，纯数论真奇妙

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        cnt = 0
        d = 1
        while d*d < num:
            if num % d == 0:
                cnt += d
                if d != 1:
                    cnt += num // d
            d += 1
        return cnt == num
# @lc code=end

