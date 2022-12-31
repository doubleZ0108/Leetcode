#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#
# 解法1(T93% S38%)：对于二叉树还是经典的递归方法，嵌套一个函数用于递归子树。如果是空节点则直接返回；如果是叶则添加最有一个值并把完整的字符串加到结果里；否则把当前值加到字符串里并添加→ 接着递归左右子树

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []

        def binarySubTreePath(root, pathstr):
            if not root: return
            if not root.left and not root.right: 
                res.append(pathstr+str(root.val))
                return
            pathstr += str(root.val)+"->"
            binarySubTreePath(root.left, pathstr)
            binarySubTreePath(root.right, pathstr)

        binarySubTreePath(root, "")
        return res
        
# @lc code=end

