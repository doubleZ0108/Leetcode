#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        result_li = ListNode()
        head = result_li
        while l1 and l2:
            if l1.val < l2.val:
                fresh_node = ListNode(l1.val, None)
                l1 = l1.next
            else:
                fresh_node = ListNode(l2.val, None)
                l2 = l2.next
            result_li.next = fresh_node
            result_li = result_li.next


        while l1:
            fresh_node = ListNode(l1.val, None)
            l1 = l1.next
            result_li.next = fresh_node
            result_li = result_li.next
        while l2:
            fresh_node = ListNode(l2.val, None)
            l2 = l2.next
            result_li.next = fresh_node
            result_li = result_li.next
        
        return head.next
# @lc code=end

