#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#
# 解法1(T89% S96%)：想了半天，觉得无论怎么做复杂度都高的不可接受（a的每个子序列在不在b中），看了题解的“脑筋急转弯”，心情emmmm，如果两字符串相同那就如示例3，一定不存在特殊序列，返回-1；否则如果二者不同，那a本身肯定不是b的子序列，反过来也是，那直接返回二者的最大长度就可！

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a==b else max(len(a), len(b))
# @lc code=end

