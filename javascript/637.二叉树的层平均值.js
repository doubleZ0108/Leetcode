/*
 * @lc app=leetcode.cn id=637 lang=javascript
 *
 * [637] 二叉树的层平均值
 * 
 * 解法1(JS T15.33% S9%)：还是正常树的层序遍历，现将每个节点的值都保存在对应层级的数组中，然后再用数组的map()方法将每一层的数组求平均值
 *   注意添加左右节点的时候是对node来说的，不要递归写多了都成root的左右节点反复加了
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
var averageOfLevels = function(root) {
    var res = [];
    var queue = [[root, 1]];
    while (queue.length) {
        var data = queue.shift();
        var node=data[0], level=data[1];

        if (res.length < level) {
            res.push([node.val]);
        } else {
            res[level-1].push(node.val);
        }

        if (node.left) {
            queue.push([node.left, level+1]);
        }
        if (node.right) {
            queue.push([node.right, level+1]);
        }
    }

    return [...res.map(x => _.sum(x)/x.length)];
};
// @lc code=end

