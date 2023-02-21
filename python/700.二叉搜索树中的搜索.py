#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#
# 解法1(T41% S32%)：非常标准的树的题，首先判断递归终止条件，如果当前节点为空则代表在这支里找不到返回空，如果当前节点的值就是要找的则返回当前的指针，否则先在左子树里找，如果能返回东西代表找到了返回即可，右子树也是一样的

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val == val:
            return root
        left = self.searchBST(root.left, val)
        if left:
            return left
        right = self.searchBST(root.right, val)
        if right:
            return right

# @lc code=end

