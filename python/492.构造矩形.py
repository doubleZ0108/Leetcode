#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#
# 解法1(T25% S78%)：如果从1开始循环到area感觉会超时因为题设范围非常大，因为最终两个数要尽可能的近，最佳情况肯定是恰巧为area的开根，两数直接相等，所以不妨从area的开根一直循环到area，找到能被area整除的L和W，需要注意的是比如2的开根取整数是1，因此最终返回的时候还是有必要判断下最小值和最大值的顺序

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for L in range(int(area**0.5), area+1):
            if area % L == 0:
                return [max(L, area//L), min(L, area//L)]

# @lc code=end

