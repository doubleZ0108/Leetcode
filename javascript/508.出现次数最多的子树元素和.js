/*
 * @lc app=leetcode.cn id=508 lang=javascript
 *
 * [508] 出现次数最多的子树元素和
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
var findFrequentTreeSum = function(root) {
    if (!root.left && !root.right) { return [root.val]; }

    var treesums = [];
    var getTreeSum = function(node) {
        if (!node) { return 0; }
        var leftsum = getTreeSum(node.left);
        var rightsum = getTreeSum(node.right);
        treesums.push(node.val + leftsum + rightsum);
        return node.val + leftsum + rightsum;
    };
    getTreeSum(root);

    var freq = new Map();
    for (var sum of treesums) {
        if (!freq.has(sum)) {
            freq.set(sum, 1);
        } else {
            freq.set(sum, freq.get(sum)+1);
        }
    }
    var freqarr = [...freq.entries()].sort((a,b)=>(b[1]-a[1]));
    var i=0;
    var res = [];
    while (i<freqarr.length && freqarr[i][1]==freqarr[0][1]) {
        res.push(freqarr[i][0]);
        i++;
    }
    return res;
};
// @lc code=end

