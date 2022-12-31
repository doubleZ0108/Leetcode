#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#
# 解法1(T90% S79%)：递归，先递归左子树，再把跟的值加入全局结果数组，最后把递归右子树
# 
# 解法2(T99% S93%)：递归（谁说递归很简单），大致思想就是一左到底，到最左边后输出叶节点值，然后回退到父节点，输出父节点的值，然后转移到右子树继续重复以上操作。具体实现：由于需要保存一连串父节点因此需要一个栈，首先while一左到底将所有父节点压栈，到左底之后输出左子树的值，然后前进到右子树，即将右子树压栈继续外层循环，但右子树可能为空，因此需要不断循环直至右子树不为空，期间把这些节点的值也输出

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 解法2 迭代
        res = []
        
        stack = [root]
        while stack:
            move = stack.pop()
            while move and move.left:
                stack.append(move)
                move = move.left
            if move: res.append(move.val)
            while stack and not move.right:
                move = stack.pop()
                res.append(move.val)
            if move and move.right:
                stack.append(move.right)

        return res
    

    def otherSolution(self, root):
        # 解法1 递归
        res = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
        
# @lc code=end

