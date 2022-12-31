#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# 解法1(T81% S89%)：与最大深度不同，不需要完整遍历，只需要找到第一个叶节点也就找到了最小深度，比较适合用层次遍历，而且在入队的同时将所在level和val打包成元组一同压，当遇到弹出队头的某个元素是叶就直接返回其level即可

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        queue = [(root,1)]
        while queue:
            node, level = queue.pop(0)
            if not node.left and not node.right: return level
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))
        
# @lc code=end

