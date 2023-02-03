#
# @lc app=leetcode.cn id=1145 lang=python3
#
# [1145] 二叉树着色游戏

# 解法1(T82% S76%)：看起来有点复杂规则很多，但本质是一道脑筋急转弯个人感觉。只需要想明白几个核心事情，将问题简化，对于先手的red方，它的选择无非就是三种，根/左子树的一个某个节点/右子树的某个节点：
#     1）如果red选了根，那blue最好的选择肯定是紧挨着根的那个节点，并且看哪个子树节点多就选哪个这样如果该子树总数比1+另一子树多则就赢；
#     2）如果red没选根那一半就主要有两种可能，
#         <1> blue直接选red的父节点，这样red只能往下扩展，剩下所有都是blue的；
#         <2> blue选red的某个子节点，这颗树包含的元素更多（这种情况跟1）有点类似）    
#     想完游戏规则之后实现起来就很简单了，只需要写两个小方法，一个是找red第一步选的位置在哪？另一个就是计算以某个节点为根的子树中的元素个数。这二者都有其他题目可以参考，前者可以通过回溯的递归找到，后者直接递归就好，而且本题判断blue能否赢有一个很简单的方式，直接判断蓝色能否占超过n/2个就好，也就是说不需要两种颜色总数都求出来再比较，直接判断某一种颜色能不能超过半数就好
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        res = []
        def deepin(node, ori):
            if not node:
                return
            if node.val==x:
                res.append((node, ori))
                return
            deepin(node.left, 'l')
            deepin(node.right, 'r')

        deepin(root, 'root')
        rednode, ori = res[0]
        
        def getsum(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return 1+getsum(node.left)+getsum(node.right)

        
        if ori == 'root':
            leftsum, rightsum = getsum(root.left), getsum(root.right)
            return max(leftsum, rightsum) > 1+min(leftsum, rightsum)
        else:
            reddownsum = getsum(rednode)
            if reddownsum < n-reddownsum:
                return True

            redleftsum, redrightsum = getsum(rednode.left), getsum(rednode.right)
            if max(redleftsum, redrightsum) > n//2:
                return True
        return False
            
# @lc code=end

