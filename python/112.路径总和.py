#
# @lc app=leetcode.cn id=112 lang=python
#
# [112] 路径总和
#
# 解法1(T85% S80%): 树中从根到叶的遍历，同样可以通过递归来做，左子树和右子树是否满足`总sum-根的val值`，终止条件是当前的节点为叶 & 值就是sum
#   注意比较的是`root.val`而不是root

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: 
            return False
        if not root.left and not root.right:
            return root.val==targetSum
        
        remain = targetSum - root.val
        return self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
Solution().hasPathSum(root, 22)
        
# @lc code=end

