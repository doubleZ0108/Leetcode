#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
# 解法1(T97% S77%): 这题唯一的不同就是如果次数相同要按字典序输出，所以要有两个排序条件，因为sorted只能从大大小排序而且默认是字典序，因此可以把次数添加一个负号 

# @lc code=start
class Solution:
    def topKFrequent(self, words, k: int):
        table = {}
        for word in words:
            if word in table: table[word] += 1
            else: table[word] = 1
        
        li = sorted(table.items(), key=lambda x: (-x[1], x[0]), reverse=False)

        res = []
        for i in range(k):
            res.append(li[i][0])

        return res
# @lc code=end

