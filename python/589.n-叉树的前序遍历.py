#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#
# 解法1(T56% S75%)：问题还是树的遍历，只不过换成了N叉树，递归的逻辑跟二叉树是一样的，只是将左右指针换成了循环children数组

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def deepin(node):
            if not node: return
            res.append(node.val)
            for child in node.children:
                deepin(child)
        deepin(root)
        return res
        
# @lc code=end

