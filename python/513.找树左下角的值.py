#
# @lc app=leetcode.cn id=513 lang=python
#
# [513] 找树左下角的值
#
# 解法1(T96% S99%)：一道非常标准树的迭代前序遍历法，借助一个栈，首先把root入栈，并且标记每个节点的level，while循环中弹出一个节点，如果它的level比之前所有都大则更新最左节点和最深探索到的层；接着如果该节点有右子树则入栈并level+1，用于之后回溯到右子树；最后while循环一左到底并更新层级和最左节点的值，同时如果有右子树也要加入

# @lc code=start
# Definition for a binary tree node.
from tkinter.tix import Tree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxLevel, leftVal = 0, root.val
        stack = [(root,0)]
        while stack:
            node, level = stack.pop()
            if level > maxLevel:
                maxLevel = level
                leftVal = node.val

            if node.right:
                stack.append((node.right, level+1))

            while node.left:
                node = node.left
                level += 1
                if level > maxLevel:
                    maxLevel = level
                    leftVal = node.val

                if node.right:
                    stack.append((node.right, level+1))
            
        return leftVal

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.left.left = TreeNode(7)
root.right.right = TreeNode(6)
Solution().findBottomLeftValue(root)
# @lc code=end

