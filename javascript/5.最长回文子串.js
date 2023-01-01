/*
 * @lc app=leetcode.cn id=5 lang=javascript
 *
 * [5] 最长回文子串
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (s.length == 1) return s

    var res = s[0];
    for (var idx=0; idx<s.length; idx++) {
        var i=idx-1, j=idx+1;

        // 如果中间都是一样的字符，则这些肯定能组成回文串
        while (i>-1 && s[i]==s[idx]) {
            i--;
        }
        while (j<s.length && s[j]==s[idx]) {
            j++;
        }

        while (i>-1 && j<s.length && s[i]==s[j]) {
            i--;
            j++;
        }
        
        if (j-i-1 > res.length) {
            res = s.slice(i+1, j);
        }
    }

    return res;
};
// @lc code=end

