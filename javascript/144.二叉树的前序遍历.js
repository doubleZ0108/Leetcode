/*
 * @lc app=leetcode.cn id=144 lang=javascript
 *
 * [144] 二叉树的前序遍历
 * 
 * 前序遍历的非递归通过<栈>来实现，先把右子树节点压栈，然后再压左子树
 * 因为前序遍历的顺序是[根，左，右]，这个左是把左子树所有节点输出完，再轮到右
 * 所以右肯定要压栈好一会
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
 * @return {number[]}
 */
var preorderTraversal = function(root) {
    var res = [];
    var preorder = function(root) {
        if (!root) { return; }
        res.push(root.val);
        preorder(root.left);
        preorder(root.right);
    };
    preorder(root);
    return res;
};


var preorderTraversal2 = function(root) {
    if (!root) { return []; }
    if (!root.left && !root.right) { return [root.val]; }

    var res = [];
    var stack = [root];
    while (stack.length) {
        var node = stack.pop();
        res.push(node.val);
        if (node.right) {
            stack.push(node.right);
        }
        if (node.left) {
            stack.push(node.left);
        }
    }
    return res;
};
// @lc code=end

