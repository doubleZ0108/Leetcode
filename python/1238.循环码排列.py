#
# @lc app=leetcode.cn id=1238 lang=python3
#
# [1238] 循环码排列
#
# 解法1(T13% S12%)：如果学过计算机组成原理和体系结构，应该一看题干就知道是格雷码（Gray Code）的题，唯一区别是起始不是0而是一个指定的元素。但我们不妨还是先从0开始生成n位的标准格雷码，再移动一下数组就可以得到以start开头的结果了。那怎么生成格雷码呢？可以直接参考 89. 格雷编码 题，首先讲第一种算法。依次对当前编码循环进行以下两操作：
#     1. 直接将最后一位二进制数取反，得到下一位格雷码
#     2. 从右到左找到第一个1，将它左边一位的元素取反（如果第一个1在首位，则将这个开头的1变成0），得到下一个格雷码
#     要注意本题不能直接从start的二进制开始，通过start的奇偶决定先从哪个操作开始，必须从0开始编码最后再交换数组次序

# @lc code=start
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = ["0"*n]
        flag = True
        while len(res) < 2**n:
            last = res[-1]
            if flag:
                res.append(last[:-1] + str(1-int(last[-1])))
            else:
                idx = last.rindex("1")
                if idx > 0:
                    idx -= 1
                res.append(last[:idx] + str(1-int(last[idx])) + last[idx+1:])
            flag = not flag

        res = list(map(lambda x: int(x, 2), res))
        idx = res.index(start)
        return res[idx:] + res[:idx]   
# @lc code=end

