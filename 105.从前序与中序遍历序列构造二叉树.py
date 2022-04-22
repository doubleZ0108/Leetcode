#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#
# 解法1(T65% S52%): preorder的第一个数就是整个树的根，再根据inorder可以划分出左右子树；之后再进行递归左右子树，同样在preorder里找根，inorder划分子树。同时在inorder里找到根的下标位置，它左边的个数就是左子树节点的总个数，这个个数在preorder里也是这么多

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0: return 
        elif len(preorder)==1: return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
# @lc code=end

