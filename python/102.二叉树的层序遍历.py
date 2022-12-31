#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#
# 解法1(T81% S40%): 维护一个队列，每次弹出一个值后把它的左右节点放到队列里，不断重复直到队列为空，注意因为是分层输出的，因此每层需要加空值表示一层的结束（题目中因为val的范围是正负1000，因此比较方便设置垃圾值）
# 
# 解法2(T94% S25%)：为每个节点添加另一个元组值表示是第几层的节点

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 解法1
        if not root: return []
        
        queue = [root]
        res = []
        while queue:
            queue.append(TreeNode(9999))
            tmp = []
            while True:
                node = queue.pop(0)
                if node.val == 9999: break
                else:
                    tmp.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            res.append(tmp)
        return res


    def otherSolution(self, root):
        if not root: return []
        
        ans = []
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if len(ans) < level:
                ans.append([node.val])
            else:
                ans[level-1].append(node.val)

            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))
        return ans
# @lc code=end

