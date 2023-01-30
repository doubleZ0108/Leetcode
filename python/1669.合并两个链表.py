#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#
# 解法1(T45% S50%)：主要考察链表头尾的操作，首先遍历list1，报错a b下标的指针，注意头指针要保留a前一位的位置这样才能往下接；然后将头指针后面接上list2，然后遍历list2直到倒数第一个节点，将其后面接上tail.next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head, tail = None, None
        move = list1
        for i in range(b+1):
            if i == a-1:
                head = move
            elif i == b:
                tail = move
            move = move.next
        
        head.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = tail.next
        return list1
        
# @lc code=end

