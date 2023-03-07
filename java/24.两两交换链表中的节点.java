/*
 * @lc app=leetcode.cn id=24 lang=java
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head==null || head.next==null) { return head; }

        ListNode newHead = new ListNode(0, head);
        ListNode pre=newHead;
        ListNode move = head;
        while (move!=null && move.next!=null) {
            ListNode tail = move.next.next;
            ListNode a = move;
            pre.next = a.next;
            a.next.next = a;
            a.next = tail;
            
            move = tail;
            pre = a;
        }

        return newHead.next;
    }
}
// @lc code=end

