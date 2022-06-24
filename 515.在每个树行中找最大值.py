#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#
# 解法1(T81% S70%)：树的层序遍历，可以通过一个队列来维护，首先将(root, 0)初始化队列，其中0标记level，用来判断同层中最大的元素，之后while循环出队一个元素并判断是否为该层第一个元素或更大的元素，最后将left和right节点继续入队循环即可

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        queue = [(root, 0)]
        res = [root.val]

        while queue:
            node, level = queue.pop()
            if level > len(res)-1:
                res.append(node.val)
            if node.val > res[level]:
                res[level] = node.val

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return res
        
        
# @lc code=end

