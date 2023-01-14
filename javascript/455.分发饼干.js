/*
 * @lc app=leetcode.cn id=455 lang=javascript
 *
 * [455] 分发饼干
 */

// @lc code=start
/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
    g.sort((a, b) => a-b);
    s.sort((a, b) => a-b);
    var i=0, j=0;
    while (i<g.length && j<s.length) {
        if (s[j] < g[i]) {
            j++;
        } else {
            i++;
            j++;
        }
    }
    return Math.min(i, j);
};
// @lc code=end

