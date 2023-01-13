/*
 * @lc app=leetcode.cn id=392 lang=javascript
 *
 * [392] 判断子序列
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    var i=0, j=0;
    while (i<s.length && j<t.length) {
        if (s[i] == t[j]) {
            i++;
            j++;
        } else {
            j++;
        }
    }
    if (i==s.length) {
        return true;
    } else {
        return false;
    }
};
// @lc code=end

