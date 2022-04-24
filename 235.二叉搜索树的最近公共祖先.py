#
# @lc app=leetcode.cn id=235 lang=python
#
# [235] 二叉搜索树的最近公共祖先
#
# 二叉搜索树满足根一定比左子树大，且一定比右子树小
#
# 解法1(T93% S38%): 如果当前遍历的节点正好介于两个节点值之间 那它就是最近的公共祖先；如果当前节点比两个数都大，那就进入左子树寻找；否则进入右子树寻找。注意提前把两节点比比大小，把小的值赋给p，大的值赋给q
#   解法1’: 迭代也是一样的，无非是root前进到root.left或root.right
#
# 解法2: 两次遍历，把p和q的所有父节点分别存成两个列表，再在两个列表中找相同且深度最深的节点返回

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p

        while root:
            if root.val >= p.val and root.val <= q.val:
                return root

            if root.val > q.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
        
# @lc code=end

