#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#
# 解法1(T92% S20%)：非常经典的链表快慢指针，初始两指针都是指向第一个节点，快的依次往后走两个位置，慢的依次往后走一个位置，当快的走到链表尾（当前指向尾或尾的下一个空位），则此时慢指针指向的就是想要寻找的链表中点

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

# @lc code=end

