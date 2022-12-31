#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#
# 解法1(T48% S92%): 仔细看题干才读出来跟上道题的区别。因为首元素就可能重复，因此要先添加头指针，最终返回的肯定是头指针的next。主题逻辑还是类似，首先记录last，如果当前的下一个和当前值相等，就不断向下试探，试探结束后要分类讨论：如果没试探，即当前元素唯一，那更新last为move，move往下一位即可；如果发现了重复元素，则让last.next指向move.next即可

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.next = head
        move = head
        last = self

        while move:
            flag = False
            while move and move.next and move.next.val == move.val:
                move = move.next
                if not flag: flag = True
            
            if flag:
                last.next = move.next
            else:
                last = move
            move = move.next
            
        return self.next
# @lc code=end

