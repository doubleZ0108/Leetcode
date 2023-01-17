/*
 * @lc app=leetcode.cn id=1143 lang=javascript
 *
 * [1143] 最长公共子序列
 */

// @lc code=start
/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    if (text1 == text2) { return text1.length; }

    var dp = Array.from(new Array(text2.length).fill(0), () => new Array(text1.length).fill(0));
    var i=0, j=0;
    while (j<text1.length) {
        if (text1[j] == text2[0]) { break;}
        j++;
    }
    while (j<text1.length) {
        dp[0][j] = 1;
        j++;
    }
    while (i<text2.length) {
        if (text1[0] == text2[i]) { break; }
        i++;
    }
    while (i<text2.length) {
        dp[i][0] = 1;
        i++;
    }

    for (var i=1; i<text2.length; i++) {
        for (var j=1; j<text1.length; j++) {
            if (text1[j] == text2[i]) {
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1);
            } else {
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]);
            }
        }
    }
    return dp[text2.length-1][text1.length-1];
};
// @lc code=end

