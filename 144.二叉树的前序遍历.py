#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#
# 前序意思是先输出根，再输出左子树，最后是右子树
# 
# 解法1(T36% S45%): 递归，没啥好说的
# 
# 解法2(T99% S50%): 迭代，需要用一个栈来维护。对于栈不断循环，首先把右子树指针压栈，然后再压左子树指针，这样下次循环就会进到左子树，而且是一路一左到底，到底之后再出栈的就是最左侧小树的右子树

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 解法2 迭代
        if not root: return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop(-1)
            res.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        
        return res


    def otherSolution(self, root):
        # 解法1 递归
        res = []

        def preorderSubTree(root):
            if not root: return
            res.append(root.val)
            preorderSubTree(root.left)
            preorderSubTree(root.right)

        preorderSubTree(root)

        return res
        
# @lc code=end

