#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#
# 解法1(T94% S93%): 递归的将左右子树调换就行，python的语法很适合写这种代码

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        
# @lc code=end

