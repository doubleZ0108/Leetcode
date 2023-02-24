#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# 解法1(解答错误 [1,2])：题目有点鸡贼，要不怎么说是中等题而不是简单题呢，不能直接递归所有的右节点，因为从右侧看到的最上面的数不一定非要是右子树的节点
#
# 解法2(T91% S90%)：二叉树的层序遍历，每一层的最后一个节点就是从右边看到的最上面的那个节点
#     改进1：不需要队列遍历的时候把所有值和对应的层级都存下来，只需要通过一个lastNode记录下上一个节点，如果当前队列弹出的节点是全新的level，则lastNode就是上一层最后一个，这样只需要一个变量就可以做到之前要用一个大数组做到的事，降低空间复杂度

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        if not root.left and not root.right: return [root.val]

        res = []
        queue = [(root, 0)]
        lastNode = None
        while queue:
            node, level = queue.pop(0)
            if level == 0:
                res.append(node.val)
            if level > len(res):
                res.append(lastNode.val)

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            lastNode = node
        res.append(lastNode.val)
            
        return res
# @lc code=end

