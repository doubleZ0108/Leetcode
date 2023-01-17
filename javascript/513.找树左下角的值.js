/*
 * @lc app=leetcode.cn id=513 lang=javascript
 *
 * [513] 找树左下角的值
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
var findBottomLeftValue = function(root) {
    if (!root.left && !root.right) { return root.val; }
    
    var getlevel = function(node) {
        if (!node) { return 0; }
        if (!node.left && !node.right) { return 1; }
        return 1 + Math.max(getlevel(node.left), getlevel(node.right));
    };
    var maxlevel = getlevel(root);

    var queue = [[root, 1]];
    while (queue.length) {
        var data = queue.shift();
        var node = data[0], level = data[1];
        if (level == maxlevel) {
            return node.val;
        }

        if (node.left) {
            queue.push([node.left, level+1]);
        }
        if (node.right) {
            queue.push([node.right, level+1]);
        }
    }
};
// @lc code=end

