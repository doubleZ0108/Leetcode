/*
 * @lc app=leetcode.cn id=83 lang=javascript
 *
 * [83] 删除排序链表中的重复元素
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
var deleteDuplicates = function(head) {
    var move = head;
    while (move) {
        var hook = move.next;
        while (hook && hook.val == move.val) {
            hook = hook.next;
        }
        move.next = hook;
        move = move.next;
    }
    return head;
};
// @lc code=end

