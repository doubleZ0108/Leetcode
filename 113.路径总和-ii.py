#
# @lc app=leetcode.cn id=113 lang=python
#
# [113] 路径总和 II
#
# 解法1(T87% S12%): 跟112完全是一道题，区别在于单独将递归封装成一个函数，同时增加一个参数parents保存一路上来的所有节点，如果递归到叶节点并且发现当前值==target剩余值，就将一路上的节点数组添加到结果数组中 

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []

        def pathRecu(root, target, parents):
            if not root: return
            if not root.left and not root.right and root.val==target:
                parents.append(root.val)
                res.append(parents)
                return

            remain = target - root.val
            pathRecu(root.left, remain, parents+[root.val])
            pathRecu(root.right, remain, parents+[root.val])

        pathRecu(root, targetSum, [])
        return res
# @lc code=end

