#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#
# 解法1(T73% S17%): 递归，把当前head后面的所有东西看成一个节点，newHead=递归后面的东西，当前的head要作为最后一个节点，所以head.next.next = head，这里的两个next就相当于把后面的东西都当成一个节点了，递归终止条件是head或head.next为空
# 解法2(T42% S72%): 建立一个新链表，依次循环原链表，在新链表头不断插入
#   改进(T90% S45%)：利用python独特的语法，把整个链接过程在一行写完

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 解法2 改进
        dummy = ListNode(next=None)
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next


    def otherSolution(self, head):
        # 解法1 递归
        if head is None or head.next is None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

        # 解法2 循环
        result = None
        while head:
            save = head
            head = head.next
            save.next = result
            result = save
        return result
# @lc code=end

