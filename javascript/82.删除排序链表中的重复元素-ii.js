/*
 * @lc app=leetcode.cn id=82 lang=javascript
 *
 * [82] 删除排序链表中的重复元素 II
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
// 解法1 直接转为数组做
var deleteDuplicates = function(head) {
    if (!head || !head.next) { return head; }

    var arr = [head.val];
    head = head.next;
    while (head) {
        var flag = false;
        while (head && head.val == arr[arr.length-1]) {
            head = head.next;
            flag = true;
        }
        if (flag) {
            arr.pop()
        } else {
            arr.push(head.val);
            head = head.next;
        }
    }

    var res = new ListNode();
    var move = res;
    for (var i in arr) {
        move.next = new ListNode(arr[i]);
        move = move.next;
    }
    return res.next;
};

// 解法2 直接处理链表，不过没用到<已排序链表>这个条件
var deleteDuplicates2 = function(head) {
    if (!head || !head.next) { return head; }

    var res = new ListNode();
    res.next = head;
    var move = head;
    var pre = res;

    while (move) {
        var tail = move.next;
        while (tail && tail.val==move.val) {
            tail = tail.next;
        }
        if (tail != move.next) {
            pre.next = tail;
            move = tail;
        } else {
            move = move.next;
            pre = pre.next;
        }
    }

    return res.next;
};
// @lc code=end

