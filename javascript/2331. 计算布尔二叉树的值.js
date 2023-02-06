/*
 * @lc app=leetcode.cn id=2185 lang=javascript
 *
 * [2331] 计算布尔二叉树的值
 * 
 * 解法1(JS T23% S88%)：标准树的题，由于是完全二叉树所以不需要考虑节点为空的情况，只需要分叶子节点和非叶子节点分别处理即可；
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
var evaluateTree = function(root) {
    if (!root.left && !root.right) {
        return root.val==0 ? false : true;
    } else {
        return root.val == 2 ? evaluateTree(root.left) || evaluateTree(root.right) : evaluateTree(root.left) && evaluateTree(root.right);
    }
};
// @lc code=end