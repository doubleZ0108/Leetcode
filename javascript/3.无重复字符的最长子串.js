/*
 * @lc app=leetcode.cn id=3 lang=javascript
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    // 动态规划
    if (s.length <= 1) return s.length;

    var dp = new Array(s.length).fill(1);
    for (var i=0; i<s.length; i++) {
        var j=i-1;
        while (j>-1 && s[j]!=s[i] && j>i-dp[i-1]-1) {
            j--;
        }
        dp[i] = i-j;
    }

    return Math.max(...dp);
};
// @lc code=end

