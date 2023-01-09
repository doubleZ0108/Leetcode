/*
 * @lc app=leetcode.cn id=257 lang=javascript
 *
 * [257] 二叉树的所有路径
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
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    var res = [];
    var getPath = function(node, parts) {
        if (!node ) { return; }
        if (!node.left && !node.right) {
            parts = parts.concat(node.val);
            res.push(parts);
            return;
        }
        getPath(node.left, parts.concat(node.val).concat("->"));
        getPath(node.right, parts.concat(node.val).concat("->"));
    };
    getPath(root, "");
    return res;
};
// @lc code=end

