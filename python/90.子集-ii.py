#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# 解法1(T32% S10%)：当前解法不是那么优美。还是通过回溯法，递归函数有两个变量i和parts，i代表当前下标，当下标超过数组长度时可以添加结果了，parts存储每一位是否选取，因为数组不能哈希，只能先通过全长的01字符串标识每一位是否选取，或者可以通过转为字符串并添加分割符的方式解决。得到了字符串数组后要将他们还原成二维数组，同时对内外结果都排序，最后再一次遍历去掉重复的元素返回。
#     本题的难点在于外层和内层结果都要考虑去重

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def deepin(i, parts):
            if i>=len(nums):
                res.add(parts)
                return
            deepin(i+1, parts)
            deepin(i+1, parts+str(nums[i])+',')
        deepin(0, "")

        res = [x.split(",") for x in list(res)]
        res = [list(filter(lambda x: x!="", x)) for x in res]
        res = sorted([sorted([int(y) for y in x]) for x in res])

        res_ = []
        i = 0
        while i<len(res):
            while i+1<len(res) and res[i+1] == res[i]:
                i += 1
            res_.append(res[i])
            i += 1
        return res_
# @lc code=end

