#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#
# 解法1(T86% S84%)：首先添加头指针，一次遍历链表，遍历过程中计数并把pre指针存下来，全部遍历完获取倒数第n个的pre指针，最后进行一次删除

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        self.next = head
        preNode = [self]
        length = 1
        while head:
            preNode.append(head)
            length += 1
            head = head.next
        pre = preNode[length-n-1]
        pre.next = pre.next.next
        
        return self.next
# @lc code=end

