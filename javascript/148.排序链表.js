/*
 * @lc app=leetcode.cn id=148 lang=javascript
 *
 * [148] 排序链表
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
 * @return {ListNode}
 */
var merge = function(a, b) {
    if (!a && !b) { return null; }
    if (a && !b) { return a; }
    if (b && !a) { return b; }

    var head = new ListNode();
    var move = head;
    while (a && b) {
        if (a.val <= b.val) {
            move.next = new ListNode(a.val);
            a = a.next;
        } else {
            move.next = new ListNode(b.val);
            b = b.next;
        }
        move = move.next;
    }
    while (a) {
        move.next = new ListNode(a.val);
        a = a.next;
        move = move.next;
    }
    while (b) {
        move.next=  new ListNode(b.val);
        b = b.next;
        move = move.next;
    }
    return head.next;
};

var mergesort = function(head) {
    if (!head || !head.next) { return head; }

    var fast=head, slow=head;
    while (fast && fast.next && fast.next.next) {
        fast = fast.next.next;
        slow = slow.next;
    }
    var a = head, b=slow.next;
    slow.next = null;

    return merge(mergesort(a), mergesort(b));
};

var sortList = function(head) {
    if (!head || !head.next) { return head; }
    return mergesort(head);
};
// @lc code=end

