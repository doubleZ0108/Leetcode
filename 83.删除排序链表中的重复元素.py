#
# @lc app=leetcode.cn id=83 lang=python
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 解法1 改进1
        if not head or not head.next: return head

        move = head.next
        last = head

        while move:
            while move and move.val == last.val:
                move = move.next
            last.next = move
            last = move
            if move: move = move.next

        return head

    def otherSolution(self, head):
        # 解法1
        if not head or not head.next: return head

        move = head.next
        last = head

        while move:
            if move.val == last.val:
                last.next = move.next
            else:
                last = move
            move = move.next
        return head
# @lc code=end

