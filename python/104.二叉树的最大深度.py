#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#
# 解法1(T99% S64%)：怎么也要把树完整遍历一次才能找到根到每个叶深度的最大值，可以简单的直接用递归方式，如果是叶则递归终止并返回高度0，否则返回左子树和右子树最大高度的那个+1

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
# @lc code=end

