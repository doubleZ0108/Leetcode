/*
 * @lc app=leetcode.cn id=206 lang=javascript
 *
 * [206] 反转链表
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
var reverseList = function(head) {
    var arr =  [];
    while (head) {
        arr.push(head.val);
        head = head.next;
    }
    arr = arr.reverse()
    var res = new ListNode();
    var move = res;
    for (var val of arr) {
        var node = new ListNode(val);
        move.next = node;
        move = move.next
    }
    return res.next;
};

var reverseList = function(head) {
    if (!head || !head.next) { return head; }
    var newHead = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return newHead;
};
// @lc code=end

