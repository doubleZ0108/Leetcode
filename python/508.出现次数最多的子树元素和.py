#
# @lc app=leetcode.cn id=508 lang=python
#
# [508] 出现次数最多的子树元素和
#
"""
解法1(T65% S95%)：思路还是很清晰的：首先肯定不能用递归，因为某一个根被算完了，它的子树还要重新算，会造成很多重复计算，所以考虑自底向上的方法，叶节点的子树元素和就是它自己的val，然后不断向上进行传播。但实现起来还是相当复杂的，整体思路是树的后根序遍历：首先先获取到左子树的元素和，然后再获取到右子树的元素和，最终根的元素和就是左+右+自己的val。
    
    引入了两个字典的数据结构，一个用来记录每个node的子树元素和（其实可以用val来做但新开辟一个也不会很大），另一个用来记录某个子树元素和出现过几次（用来找最多的输出）
    
    同时树的迭代遍历还需要一个栈来维护，初始将root加入栈中，然后开启while循环，每次弹出一个节点，如果该节点的左右节点都计算过子树元素和了，那就可以直接更新当前节点，也就提前结束了；否则一左到底，如果最左侧的节点是叶子则它也可以更新了，然后再将根和右节点入栈交给下次循环
    
    最终处理输出时，首先找到统计次数的字典里的最大值，python可以一行实现`max(zip(table.values(), table.keys()))[0]`，然后遍历一遍输出结果即可
    
    整体难点就在于树边界的判断，以及不能反反复复的在左子树里走（所以要记录一下）
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
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree_sum_table = {}
        sum_count_table = {}

        stack = [root]
        while stack:
            node = stack.pop()

            fastFlag = False
            if node.left==None and node.right==None:
                tree_sum_table[node] = node.val
                fastFlag = True
            elif node.left in tree_sum_table and node.right==None:
                tree_sum_table[node] = tree_sum_table[node.left] + node.val
                fastFlag = True
            elif node.right in tree_sum_table and node.left==None:
                tree_sum_table[node] = tree_sum_table[node.right] + node.val
                fastFlag = True
            elif node.left in tree_sum_table and node.right in tree_sum_table:
                tree_sum_table[node] = tree_sum_table[node.left] + tree_sum_table[node.right] + node.val
                fastFlag = True

            if fastFlag:
                sum_count_table[tree_sum_table[node]] = 1 if tree_sum_table[node] not in sum_count_table else sum_count_table[tree_sum_table[node]]+1
                continue

            while node.left and node.left not in tree_sum_table:
                stack.append(node)
                node = node.left
            if node.left==None and node.right==None:
                tree_sum_table[node] = node.val
                sum_count_table[tree_sum_table[node]] = 1 if tree_sum_table[node] not in sum_count_table else sum_count_table[tree_sum_table[node]]+1
            else:
                stack.append(node)

            if stack and stack[-1].right:
                stack.append(stack[-1].right)

        maxCount = max(zip(sum_count_table.values(), sum_count_table.keys()))[0]
        res = []
        for key, value in sum_count_table.items():
            if value == maxCount: res.append(key)
        return res

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
Solution().findFrequentTreeSum(root)
# @lc code=end

