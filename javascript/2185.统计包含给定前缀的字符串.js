/*
 * @lc app=leetcode.cn id=2185 lang=javascript
 *
 * [2185] 统计包含给定前缀的字符串
 */

// @lc code=start
/**
 * @param {string[]} words
 * @param {string} pref
 * @return {number}
 */
var prefixCount = function(words, pref) {
    var res = 0;
    for (var i=0; i<words.length; i++) {
        if (words[i].startsWith(pref)) {
            res++;
        }
    }
    return res;
};
// @lc code=end

