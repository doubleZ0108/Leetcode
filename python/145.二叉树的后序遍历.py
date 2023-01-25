#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# 解法1(T69% S19%)：递归，树的标准写法，先左子树，再右子树，最后根节点

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def post(node):
            if not node: return
            if not node.left and not node.right:
                res.append(node.val)
                return
            post(node.left)
            post(node.right)
            res.append(node.val)

        post(root)
        return res
# @lc code=end

