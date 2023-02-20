#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#
# 解法1(T22% S87%)：还是跟正常的二叉树层序遍历一样做，得到层序结果数组之后把所有奇数下标项的输出逆转即可

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        queue = [(root, 1)]
        res = []
        while queue:
            node, level = queue.pop(0)
            if level > len(res):
                res.append([node.val])
            else:
                res[-1].append(node.val)
            
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            
        for i in range(len(res)):
            if i%2 == 1:
                res[i] = res[i][::-1]

        return res
# @lc code=end

