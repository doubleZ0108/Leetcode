/*
 * @lc app=leetcode.cn id=2 lang=javascript
 *
 * [2] 两数相加
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
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var res = new ListNode();
    var head = res;
    var remain = 0;
    while (l1 && l2) {
        res.next = new ListNode((l1.val + l2.val + remain) % 10);
        remain = Math.floor((l1.val + l2.val + remain) / 10);
        res = res.next;
        l1 = l1.next;
        l2 = l2.next;
    }

    while (l1) {
        res.next = new ListNode((l1.val + remain) % 10);
        remain = Math.floor((l1.val + remain) / 10);
        res = res.next;
        l1 = l1.next;
    }
    while (l2) {
        res.next = new ListNode((l2.val + remain) % 10);
        remain = Math.floor((l2.val + remain) / 10);
        res = res.next;
        l2 = l2.next;
    }

    if (remain != 0) {
        res.next = new ListNode(remain);
    }

    return head.next;
};
// @lc code=end

