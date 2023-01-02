/*
 * @lc app=leetcode.cn id=24 lang=javascript
 *
 * [24] 两两交换链表中的节点
 * 
 * 交换链表中节点的题，只要理清楚和用变量保存清楚 pre -> a -> b -> tail的关系即可
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
var swapPairs = function(head) {
    if (!head || !head.next) { return head; }

    var pre = new ListNode();
    pre.next = head;
    var move = head;
    var res = head.next;
    while (move && move.next) {
        var a = move;
        var b = move.next;
        var tail = move.next.next;

        pre.next = b;
        b.next = a;
        a.next = tail;

        pre = move;
        move = move.next;
    }
    return res;
};
// @lc code=end

