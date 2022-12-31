#
# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#
# 解法1(T100% S85%): 递归，如果当前节点相等 & 左子树相等 & 右子树相等 则True，否则False（注意当前根是否为None的预先判断）
# 
# 解法2: 分别遍历每棵树，各获得一个数组，比较两个数组是否相等（不过获取树的遍历一般也是用递归，迭代代码有点麻烦感觉不值，因为递归到某一步不想等就停了，只是递归栈空间有点浪费）

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# @lc code=end

