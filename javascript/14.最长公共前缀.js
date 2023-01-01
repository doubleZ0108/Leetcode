/*
 * @lc app=leetcode.cn id=14 lang=javascript
 *
 * [14] 最长公共前缀
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    for (var i=0; i<strs[0].length; i++) {
        for (var j=1; j<strs.length; j++) {
            if (strs[j].length < i || strs[j][i] != strs[0][i]) {
                return strs[0].slice(0, i);
            }
        }
    }
    return strs[0];
};
// @lc code=end

