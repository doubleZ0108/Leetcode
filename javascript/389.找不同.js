/*
 * @lc app=leetcode.cn id=389 lang=javascript
 *
 * [389] 找不同
 * 
 * js对集合的支持也很差
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    s = s.split("").sort();
    t = t.split("").sort();
    for (var i=0,j=0; i<s.length && j<t.length; i++,j++) {
        if (s[i]!=t[j]) {
            return t[j];
        }
    }
    return t[t.length-1];
};
// @lc code=end

