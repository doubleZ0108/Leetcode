#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#
# 解法1(T90% S5%)：虽说是二叉树最大深度的自然变种，但是对于二叉树的两指针写法上还是有一些区别，如果当前节点为空则深度就是0，如果当前节点没有child则深度为1，然后循环并递归所有孩子

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if len(root.children)==0: return 1
        return max([self.maxDepth(node)+1 for node in root.children])
        
# @lc code=end

