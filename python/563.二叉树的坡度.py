#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#
# 解法1(T92% S12%)：二叉树的题不要怕，直接递归就完事了。这题跟二叉树求和很类似，区别在于在完整求取节点和之前先计算下左右子树和之差的绝对值，而且要把这个值存在全局里，因为最后要计算所有节点的坡度

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = []

        def deepin(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            leftsum = deepin(node.left)
            rightsum = deepin(node.right)
            res.append(abs(leftsum - rightsum))
            return leftsum + rightsum + node.val

        deepin(root)

        return sum(res)
# @lc code=end

