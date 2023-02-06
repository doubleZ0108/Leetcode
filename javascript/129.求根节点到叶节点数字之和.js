/*
 * @lc app=leetcode.cn id=129 lang=javascript
 *
 * [129] 求根节点到叶节点数字之和
 * 
 * 解法1(T44% S13%)：比较经典树题的结构，首先先递归并保存根到每个叶节点的值，通过递归变量parts存储，注意树在递归是要记得判断左右节点是否为空，所有路径全部统计完再进行求和即可
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
var sumNumbers = function(root) {
    var res = [];
    var deepin = function(node, parts) {
        if (!node.left && !node.right) {
            res.push(parseInt(parts.concat(node.val.toString())));
            return;
        }
        if (node.left) {
            deepin(node.left, parts.concat(node.val.toString()));
        }
        if (node.right) {
            deepin(node.right, parts.concat(node.val.toString()));
        }
    };
    deepin(root, "");
    return res.reduce((x, y) => x+y);
};
// @lc code=end

