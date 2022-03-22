#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#
# 解法1(超时): 链表插入排序，用move.next进行遍历，把它插入到前面排序好链中合适的位置
#   改进1：如果当前要移动的元素比有序链尾大则不需要排序
#   改进2: 不是一个一个插，每次插都一直往后把一串相等的都拿出来，一起插入到之前
#   改进3(T5% S83%): 打表，记录插过的数字的位置，之后遇见插过的，直接一步到位（要注意要存储freshPos.next，否则freshPos也可能后面插了相同的位置就变了）
# 
# 解法2(T79% S61%): 链表归并排序（自顶向下），首先通过快慢指针找到链表中心，左右分别递归归并，最后合并有序链表
# 
# 解法3(T32% S24% 按理应该是T O(n log n)  S O(1): 链表归并排序（自底向上），首先一次遍历计算链表总长度L，分别做1+1元素归, 2+2元素归并, ..., L/2+L/2元素归并，因为是链表的归并，因此每次都要记住pre和tail指针，同时在两个链表的merge时也要获取到merge后的start和end（整体思想不复杂，但实现时指针为空的判断属实是被恶心到了）

# @lc code=start
# Definition for singly-linked list.
from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return '{} -> {}'.format(self.val, self.next)

class Solution(object):
       
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        def merge(left, right):
            move = ListNode(0)
            start = move
            while left and right:
                if left.val < right.val:
                    move.next = left
                    left = left.next
                    move = move.next
                else:
                    move.next = right
                    right = right.next
                    move = move.next
            if left:
                move.next = left
            if right:
                move.next = right
            while move.next:
                move = move.next
            return start.next, move

        self.next = head

        # 获取长度
        L = 0
        move = head
        while move:
            L += 1
            move = move.next

        move = self
        l = 1
        while l < L:
            pre = self
            while pre and pre.next and pre.next.next:
                left = pre.next
                move = left
                for _ in range(l-1):
                    if not move or not move.next:
                        break
                    move = move.next
                    
                right = move.next
                move.next = None
                move = right
                for _ in range(l-1):
                    if not move or not move.next:
                        break
                    move = move.next
                    
                if move:
                    tail = move.next
                    move.next = None
                else:
                    tail = move

                start, end = merge(left, right)
                pre.next = start
                end.next = tail
                pre = end

            l <<= 1
        
        return self.next
        


    def otherSolution(self, head):
        # 解法2
        if not head or not head.next:
            return head

        # 快慢指针找中点
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)

        # 有序链表合并
        ans = self
        while left and right:
            if left.val < right.val:
                ans.next = left
                left = left.next
                ans = ans.next
            else:
                ans.next = right
                right = right.next
                ans = ans.next
        if left:
            ans.next = left
        if right:
            ans.next = right

        return self.next



        # 解法1
        if not head:
            return head

        posTable = {}

        self.next = head
        move = self.next
        while move.next:
            # 改进1 已经比有序链尾大，不需要排序
            if move.next.val >= move.val:
                move = move.next
                continue 

            # 改进2 把一串相等的一起拿出来
            startPos, endPos = move.next, move.next
            while endPos.next and endPos.next.val == startPos.val:
                endPos = endPos.next

            if endPos.val in posTable:
                # 改进3
                freshPos = posTable[endPos.val]
                move.next = endPos.next
                endPos.next = freshPos.next
                freshPos.next = startPos
            else:
                # 从头一个一个看吧
                freshPos = self
                while freshPos.next!=move.next:
                    if freshPos.next.val > endPos.val:
                        move.next = endPos.next
                        endPos.next = freshPos.next
                        freshPos.next = startPos
                        posTable[endPos.val] = freshPos.next
                        break
                    freshPos = freshPos.next

        return self.next


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(5) 
    head.next.next.next.next.next = ListNode(0) 
    head.next.next.next.next.next.next = ListNode(8)
    head.next.next.next.next.next.next.next = ListNode(-1)
    head.next.next.next.next.next.next.next.next = ListNode(0)
    head.next.next.next.next.next.next.next.next.next = ListNode(9)
    Solution().sortList(head)
# @lc code=end

