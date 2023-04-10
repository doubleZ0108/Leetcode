#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
# 
# 解法1(超时 67/76)：递归，先把当前节点存下来放入递归变量，没到一个新的链表节点都把这个之前缓存的list看看我是不是比他们里的谁大了，如果大就更新这个位置的结果，并移除list，这样相当于在递归里嵌套了一层循环，而且还涉及到数组的删除，肯定会超时
# 
# 解法2(T85% S10%)：单调栈，这确实是解决这种第一个比它大的题的标准解，维护一个单调栈，如果当前元素比栈顶元素大则不断弹栈，并将栈顶元素对应的结果位置的值变成当前节点的这个“第一个大的值”，与数组的题不同在于因为链表预先不知道有多少个节点，因此每便利一个节点就现在结果中append一个0，这样之后才能在结果中赋予这一位置值

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        idx = 0
        stack = []
        move = head
        while move:
            res.append(0)   # 也顺道起到统计节点个数的作用

            while stack and move.val > stack[-1][0]:
                val, i = stack.pop()
                res[i] = move.val
            stack.append((move.val, idx))

            idx += 1
            move = move.next
        return res


    def nextLargerNodes1(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        move = head
        while move:
            n += 1
            move = move.next
        res = [0 for _ in range(n)]

        def deepin(node, parts):
            if not node: return
            for idx, num in list(parts):
                if node.val > num:
                    res[idx] = node.val
                    parts.remove((idx, num))
            parts.append((idx+1, node.val))
            deepin(node.next, parts)
        deepin(head.next, [(0, head.val)])
        return res
# @lc code=end

