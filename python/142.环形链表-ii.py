#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# 解法1(T78% S10%)：跟141题一样，不妨在循环过程中把所有节点的指针都存在集合中，如果发现某个节点的next指针已经在集合中，那就意味着这个next之前遍历过，现在又遍历回来了，那这个next就是环的入环处

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        S = set()
        move = head
        while move:
            if move.next in S:
                return move.next
            S.add(move)
            move = move.next
        return None
        
# @lc code=end

