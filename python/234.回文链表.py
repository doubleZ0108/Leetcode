#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# 解法1(T72% S89%)：题干说要时间$O(n)$空间$O(1)$的方法，那肯定不能接住额外数组，肯定是跟链表反转有关。我们首先通过快慢指针找到链表中点，再配合链表长度的奇偶找到后半段链表，将后半段链表反转，然后遍历反转后的后半段和原始链表头，如果二者一直相等则很好，如果找到一个不相等就直接False，因为后半段链表长度刚好为链表长度的一半，所以可以用它作为循环条件，前半段肯定有对应元素

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l, move = 0, head
        while move:
            move = move.next
            l += 1

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if l%2:
            slow = slow.next

        dummy = ListNode()
        while slow:
            dummy.next, slow.next, slow = slow, dummy.next, slow.next
        tail = dummy.next
        
        move = head
        while tail:
            if move.val != tail.val:
                return False
            move = move.next
            tail = tail.next
        return True
# @lc code=end

