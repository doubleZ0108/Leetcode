/*
 * @lc app=leetcode.cn id=997 lang=javascript
 *
 * [997] 找到小镇的法官
 */

// @lc code=start
/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    var indegrees = new Array(n+1).fill(0);
    var outdegrees = new Array(n+1).fill(0);
    for (var t of trust) {
        outdegrees[t[0]]++;
        indegrees[t[1]]++;
    }

    for (var i=1; i<indegrees.length; i++) {
        if (indegrees[i]==n-1 && outdegrees[i]==0) {
            return i;
        }
    }
    return -1;
};
// @lc code=end

