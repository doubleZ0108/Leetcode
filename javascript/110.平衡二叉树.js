/*
 * @lc app=leetcode.cn id=110 lang=javascript
 *
 * [110] 平衡二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var getHeight = function(root) {
    if (!root) { return 0; }
    if (!root.left && !root.right) { return 1; }
    return 1 + Math.max(getHeight(root.left), getHeight(root.right));
};

var isBalanced = function(root) {
    if (!root) { return true; }
    return Math.abs(getHeight(root.left)-getHeight(root.right))<=1 && isBalanced(root.left) && isBalanced(root.right);
};
// @lc code=end

