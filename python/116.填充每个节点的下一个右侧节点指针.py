#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#
# 解法1(T22% S5%)：这个任务是第一次看很新奇，但仔细看了示意图这不就是树的层次遍历问题吗！直接用队列层次遍历树，弹出头节点作为当前节点，如果当前队列中的头元素跟改元素是同一层级的，那该节点的next就是当前队列的头
#    或者也可以不通过层级控制，因为是完美二叉树所以每层都一定是$2^n$个节点，也可以根据这个作为边界条件

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or (not root.left and not root.right): return root

        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if queue and queue[0][1] == level:
                node.next = queue[0][0]
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        return root
        
# @lc code=end

