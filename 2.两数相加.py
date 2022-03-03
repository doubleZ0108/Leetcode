#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        head = result
        bonus = 0

        while l1 and l2:
            fresh = ListNode()
            head.next = fresh
            head = fresh
            fresh.val = (l1.val + l2.val + bonus) % 10
            bonus = (l1.val + l2.val + bonus) // 10

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            fresh = ListNode()
            head.next = fresh
            head = fresh
            fresh.val = (l1.val + bonus) % 10
            bonus = (l1.val + bonus) // 10

            l1 = l1.next

        while l2:
            fresh = ListNode()
            head.next = fresh
            head = fresh
            fresh.val = (l2.val + bonus) % 10
            bonus = (l2.val + bonus) // 10

            l2 = l2.next
        
        if bonus != 0:
            fresh = ListNode()
            fresh.val = bonus
            fresh.next = None
            head.next = fresh

        return result.next
# @lc code=end

