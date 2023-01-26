#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# 解法1(超时 37/39)：两重循环暴力，对于A的每个节点，从头到尾循环B看B中是否有一个节点等于当前A的这个节点
#
# 解法2(T46% S7%)：先一次循环A链表，将每个节点都加入哈希集合中，再一次循环B链表，如果当前节点也在A里则找到了相交节点（集合中本质存的是地址，因此不会重复）

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 解法2
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        moveA = headA
        while moveA:
            setA.add(moveA)
            moveA = moveA.next
        moveB = headB
        while moveB:
            if moveB in setA:
                return moveB
            moveB = moveB.next
        return None

    # 解法1
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        moveA = headA
        while moveA:
            moveB = headB
            while moveB:
                if moveB == moveA:
                    return moveB
                moveB = moveB.next
            moveA = moveA.next
        return None
        
# @lc code=end

