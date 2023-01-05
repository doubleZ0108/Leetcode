/*
 * @lc app=leetcode.cn id=72 lang=javascript
 *
 * [72] 编辑距离
 */

// @lc code=start
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    var m=word1.length+1, n = word2.length+1;
    var dp = Array.from(new Array(m).fill(0), () => new Array(n).fill(0));
    for (var i=0; i<m; i++) {
        dp[i][0] = i;
    }
    for (var j=0; j<n; j++) {
        dp[0][j] = j;
    }

    for (var i=1; i<m; i++) {
        for (var j=1; j<n; j++) {
            if (word1[i-1] == word2[j-1]) { // 这里没记住，如果末尾相等则不需要执行任何操作，本来就相等了
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1;
            }
        }
    }
    return dp[m-1][n-1];
};
// @lc code=end

