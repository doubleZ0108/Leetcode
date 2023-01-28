#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# 解法1(T96% S16%)：首先添加头指针，python可以直接用self来的当头指针，然后用move.next来遍历链表，如果move.next是指定元素，则move.next = move.next.next跳过这个链接（如果是C语言要记得释放这个元素），此时move不用动，因为下个元素还可能是指定元素；否则，如果下一个元素不是的话move正常往后移动就好。另外还需要注意循环条件如果是move.next的话还必须要首先确定move不是空指针

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return head

        self.next = head
        move = self
        while move and move.next:
            if move.next.val == val:
                move.next = move.next.next
            else:
                move = move.next
        return self.next
# @lc code=end

