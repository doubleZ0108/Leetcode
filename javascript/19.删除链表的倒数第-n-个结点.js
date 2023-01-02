/*
 * @lc app=leetcode.cn id=19 lang=javascript
 *
 * [19] 删除链表的倒数第 N 个结点
 * 
 * 快慢指针
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    if (!head.next && n==1) { return head.next; }

    var fast = head, slow = head;
    for (var i=0; i<n; i++) {
        fast = fast.next;
    }
    // 如果此时快指针已经出界，则删除的就是第一个节点
    if (!fast) { return head.next; }

    while (fast && fast.next) {
        fast = fast.next;
        slow = slow.next;
    }
    slow.next = slow.next.next;
    return head;
};
// @lc code=end

