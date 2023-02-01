/*
 * @lc app=leetcode.cn id=109 lang=javascript
 *
 * [109] 有序链表转换二叉搜索树
 * 
 * 解法1(T80% S82%)：两个数据结构一起使用还是很有趣的，跟有序数组转换一样的部分是树的建立，还是找到中心作为树的根节点，然后一次递归建立左子树和右子树；难点主要在于链表的处理，我们知道快慢指针可以找到链表的中心，但要注意因为需要将链表变为 第一段-中心-第二段，且第一段要和中心断开，因此要引入一个哑节点并用slow.next和fast.next来遍历链表，找到链表中心的前一个节点
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
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    if (!head) { return null; }
    if (!head.next) { return new TreeNode(head.val); }

    var move = new ListNode();
    move.next = head;
    var fast=move, slow=move;
    while (fast.next && fast.next.next) {
        fast = fast.next.next;
        slow = slow.next;
    }
    
    var root = new TreeNode(slow.next.val);
    root.right = sortedListToBST(slow.next.next);
    slow.next = null;
    root.left = sortedListToBST(head);
    return root;
};
// @lc code=end

