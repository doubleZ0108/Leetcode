/*
 * @lc app=leetcode.cn id=111 lang=javascript
 *
 * [111] 二叉树的最小深度
 * 
 * 最大深度可以直接递归，最小深度只能用层序来找第一个叶子节点
 * 因为只有叶子节点才能说深度是多少，如果还是递归的话，看到一个空子树也会直接返回最小的
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
 * @return {number}
 */
var minDepth = function(root) {
    if (!root) { return 0; }
    var queue = [[root, 1]];
    while (queue) {
        var data = queue.shift();
        var node = data[0], level = data[1];
        if (!node.left && !node.right) { return level; }
        if (node.left) {
            queue.push([node.left, level+1]);
        }
        if (node.right) {
            queue.push([node.right, level+1]);
        }
    }
};
// @lc code=end

