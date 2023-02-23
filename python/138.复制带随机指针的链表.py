#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#
# 解法1(T80% S65%)：链表和哈希表跨界的一道很有趣的题，因为每个节点都有一个random指针指向任意一个节点，所以我们很容易想到要把每个节点都用哈希表存下来，key为原链表的节点地址，val为新链表一样位置节点的地址，这样通过在哈希表中查找move.random就能找到需要的地址。具体而言通过一个move指针遍历原链表的每个节点，如果哈希表没存过这个地址，就代表新链表还没创建过这个节点，那就创建一个新节点并将key-val加入哈希表，如果查找到了，就证明之前有个人的random指向这个后面的节点，我刚才已经创建过了并且存下来了，那直接用就好了；第二步就是链接random指针，如果random不为None，则看原链表当前节点指向的random的key在哈希表中是否存在，如果不存在就证明我要random链接的这个我还没连接到，先创建一个节点存下来，更新新创建节点的random指针；最后就是正常的链接链表，move往后移动一个，newHead也往后移动一格，因为newHead移动了，所以最开始要有个变量存一下

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        newHead = Node(0)
        self.next = newHead

        table = {}
        move = head
        while move:
            if move not in table:
                fresh = Node(move.val)
                table[move] = fresh
            else:
                fresh = table[move]

            if move.random:
                if move.random not in table:
                    table[move.random] = Node(move.random.val)
                fresh.random = table[move.random]
            
            newHead.next = fresh
        
# @lc code=end

