/*
 * @lc app=leetcode.cn id=101 lang=javascript
 *
 * [101] 对称二叉树
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
var isSymmetric = function(root) {
    if (!root) { return true; }
    if (!root.left && !root.right) { return true; }
    if ((root.left && !root.right) || (!root.left && root.right)) { return false; }

    var symm = function(left, right) {
        // 如果都是空可以
        if (!left && !right) { return true; }
        // 如果有一个为空那不行
        else if (!left || !right) { return false; }
        return left.val == right.val && symm(left.left, right.right) && symm(left.right, right.left);
    };

    return symm(root.left, root.right);
};
// @lc code=end

