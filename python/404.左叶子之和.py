#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# 解法1(T81% S99%)：递归法很难判断是否为左子树，采用层序遍历，并标注每个入队节点是否为左子树的节点，如果一个弹出的节点既是叶节点又是从左子树来的，则累加他们

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ueue = [(root, False)]
        res = 0
        while queue:
            node, isLeft = queue.pop(0)
            if not node.left and not node.right and isLeft:
                res += node.val
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
        return res
# @lc code=end

