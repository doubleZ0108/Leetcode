#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#
# 解法1(T63% S16%): 遍历的过程中把每个遇到过的指针都存下来（哈希表/集合）
# 解法2(T99% S80%): 双指针，快慢指针，一个每次走两步，一个一次走一步，看什么时候会遇上

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 解法2
        if not head or not head.next: return False
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow: return True
        return False

    def otherSolution(self, head):
        # 解法1
        S = set()
        while head:
            if head in S:
                return True
            S.add(head)
            head = head.next
        return False
        
# @lc code=end

