#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# 解法1(T60% S62%)：链表的题总是觉得很巧妙很有趣，但都有迹可寻，只要记录好要断开位置的前一个pre和后一个tail。因为只要把比x小的放到左面，因此要找到第一个大于等于x的位置，之后小的元素就是要插到这个位置之前，构建哑指针，通过move.next找到这个位置，然后继续遍历剩下的，同样用next指向，如果找到了比x小的则将其插到之前保留的指针后面，注意指针先后断开的顺序即可

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        self.next = head
        lastmin = self
        while lastmin and lastmin.next:
            if lastmin.next.val >= x:
                break
            lastmin = lastmin.next

        move = lastmin
        while move and move.next:
            if move.next.val < x:
                tail = move.next.next
                move.next.next = lastmin.next
                lastmin.next = move.next
                lastmin = lastmin.next
                move.next = tail
            else:
                move = move.next

        return self.next
# @lc code=end

