#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#
# 处理链表问题的核心是要记住之前一段的末尾和接下来一段的起点，推荐直接用pre和last两个变量来存，每次更新，不要想着用一个变量move就能搞定
# 
# 解法1(T94% S55%): 首先设置头节点存储空位，接下来设置好pre和last，在纸上想好连接的顺序，①move.next.next连到move上(交换顺序) ②pre.next连到move.next上(把之前的串上)  ③pre更新 ④move.next指向last ⑤更新move循环下一截
# 
# 解法2(T76% S72%): 利用python特殊的语法，我们的目的是 pre-a-b-b.next => pre-b-a-b.next，直接看我们要得到的链，通过python语法可以直接写，其他就是记得初始化以及更新pre了，由于最前头也需要pre，所以也需要加一个头指针

# @lc code=start
# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
        
    def otherSolution(self):
        if not head or not head.next:   # 空 or 只有一个节点
            return head

        result = ListNode()
        result.next = head

        pre = result
        move = head
        while move and move.next:
            last = move.next.next
            move.next.next = move
            pre.next = move.next
            pre = move
            move.next = last
            move = last
        
        return result.next

# @lc code=end

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    Solution().swapPairs(head)