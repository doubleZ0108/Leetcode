/*
 * @lc app=leetcode.cn id=100 lang=javascript
 *
 * [100] 相同的树
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
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    // 这个终止条件确实要认真想清楚，因为有两个参数，要综合考虑他们共通的终止情况
    if ((!p && q) || (p && !q)) { return false; }
    else if (!p && !q) { return true; }
    
    return p.val==q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
// @lc code=end

