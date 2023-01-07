/*
 * @lc app=leetcode.cn id=113 lang=javascript
 *
 * [113] 路径总和 II
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
 * @param {number} targetSum
 * @return {number[][]}
 */
var pathSum = function(root, targetSum) {
    if (!root) { return []; }
    
    var res = [];
    var findpath = function(node, remain, parts) {
        if (!node) { return; }
        if (!node.left && !node.right && remain == node.val) {
            parts.push(node.val);
            res.push(parts);
            return;
        }

        findpath(node.left, remain-node.val, parts.concat(node.val));
        findpath(node.right, remain-node.val, parts.concat(node.val));
    };
    findpath(root, targetSum, []);
    return res;
};
// @lc code=end

