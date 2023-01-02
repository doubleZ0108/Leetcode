/*
 * @lc app=leetcode.cn id=21 lang=javascript
 *
 * [21] 合并两个有序链表
 * 
 * 解法1(T23% S46%): 非常经典的链表题，首先同时循环两个链表，将数值较小的那个数创建新节点链接在结果链表的尾部，二者整体扫描完再将更长的链表剩下的一截直接串到结果链表尾部即可，推荐开始时创建一个哑节点，方便整体代码书写 
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
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    var res = new ListNode();
    var head = res;
    while (list1 && list2) {
        if (list1.val < list2.val) {
            res.next = new ListNode(list1.val);
            list1 = list1.next;
        } else {
            res.next = new ListNode(list2.val);
            list2 = list2.next;
        }
        res = res.next;
    }
    if (list1) {
        res.next = list1;
    }
    if (list2) {
        res.next = list2;
    }
    return head.next;
};
// @lc code=end

