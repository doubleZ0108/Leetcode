/*
 * @lc app=leetcode.cn id=102 lang=javascript
 *
 * [102] 二叉树的层序遍历
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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if (!root) { return []; }
    var queue = [[root, 1]];
    var res = [];
    var data, node, level;
    while (queue.length) {
        data = queue.shift();
        node = data[0], level = data[1];

        if (level > res.length) {
            res.push([node.val]);
        } else {
            res[res.length-1].push(node.val);
        }

        if (node.left) {
            queue.push([node.left, level+1]);
        }
        if (node.right) {
            queue.push([node.right, level+1]);
        }
    }
    return res;
};
// @lc code=end

