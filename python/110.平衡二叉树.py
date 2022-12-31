#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#
# 解法1(T83% S84%): 按照题意写代码就好
#   首先写一个获取某个子树高度的函数：如果是空则高度为0；如果是叶则高度为1；否则高度就是`1+max(左子树高度，右子树高度)`
#   然后再依次判断`abs(左子树高度，右子树高度)`是不是比2小，如果不满足则False，如果满足则再遍历左右子树
# 
# 其实对于树的题递归一遍就可以，因为树虽然可能很大，但一般都不很深，几次递归就到叶了

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getSubTreeHeight(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.getSubTreeHeight(root.left), self.getSubTreeHeight(root.right))

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        if abs(self.getSubTreeHeight(root.left) - self.getSubTreeHeight(root.right)) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
# @lc code=end

