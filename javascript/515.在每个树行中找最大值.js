/*
 * @lc app=leetcode.cn id=515 lang=javascript
 *
 * [515] 在每个树行中找最大值
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
var largestValues = function(root) {
    if (!root) { return []; }
    var queue = [[root, 1]];
    var res = [];
    while (queue.length>0) {
        var data = queue.shift();
        var node=data[0], level=data[1];
        if (res.length < level) {
            res.push(node.val)
        } else if (res[res.length-1] < node.val) {
            res[res.length-1] = node.val
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

