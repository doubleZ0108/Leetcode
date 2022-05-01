#
# @lc app=leetcode.cn id=83 lang=python
#
# [83] 删除排序链表中的重复元素
#
# 解法1(T77% S47%): 看着平淡无奇，逻辑性还挺高的。一次遍历，保存上一次的节点，如果当前节点值等于上一节点值，则上一节点直接指向下一节点。但有一个小细节是如果删除了当前节点后让last=move，再次循环时move会被删除，此时last指向的很可能是空
#   改进1(T77% S51%): 不是每次跟前面相等就删除一次，而是不断循环判断，把一串相等的都等到然后一次删除。链表的循环还是要注意是否为空的判断

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

