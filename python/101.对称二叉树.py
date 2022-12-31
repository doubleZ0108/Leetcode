#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#
"""
解法1(T85% S52%)：递归，递归函数有两个变量`left`和`right`，首先要满足left和right的值一样，然后递归 left的左子树和right的右子树要相等，同时left的右子树也要和right的左子树相等。递归终止条件是如果left和right都是None则返回True，如果只有一个人为None则返回False
    注意，相等不是根节点`==`，而是满足递归函数

解法2(T85% S82%)：迭代，类似于迭代法先序遍历，不过升级点在于左子树按照“根-左-右”做，右子树按照“根-右-左”做。具体来说维护`lstack`和`rstack`两个数据结构，初始值都是只有`root`，每次分别弹出`lnode`和`rnode`判断是否相等（还要判断是否为None），如果不相等代表根的值就不一样，直接False；如果相等则`lstack`加入`lnode`的右子树，把它存下来之后要回溯，同样的`rstack`加入当前`rnode`的左子树，然后`lstack`一左到底，`rstack`一右到底，期间要满足始终相等
"""

# @lc code=start
# Definition for a binary tree node.
from tkinter.tix import Tree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 解法2 迭代
        lstack, rstack = [root], [root]
        while lstack and rstack:
            lnode, rnode = lstack.pop(), rstack.pop()
            if not lnode and not rnode: continue
            elif not lnode or not rnode: return False
            if lnode.val != rnode.val: return False

            lstack.append(lnode.right)
            rstack.append(rnode.left)

            while True:
                lnode, rnode = lnode.left, rnode.right
                if not lnode and not rnode: break
                elif not lnode or not rnode: return False
                if lnode.val != rnode.val: return False
                lstack.append(lnode)
                rstack.append(rnode)
            
        return True
        

    def otherSolution(self, root):
        # 解法1 递归
        def isSym(left, right):
            if not left and not right: return True
            elif not left or not right: return False

            if left.val != right.val: return False
            return isSym(left.left, right.right) and isSym(left.right, right.left)

        return isSym(root.left, root.right)

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(3)
root.left.left = TreeNode(4)  
root.left.right = TreeNode(5)
# root.right.left = TreeNode(4)
root.right.right = TreeNode(4)    

Solution().isSymmetric(root)
# @lc code=end

