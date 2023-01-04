/*
 * @lc app=leetcode.cn id=63 lang=javascript
 *
 * [63] 不同路径 II
 */

// @lc code=start
/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    var m=obstacleGrid.length, n=obstacleGrid[0].length;
    if (obstacleGrid[0][0]==1 || obstacleGrid[m-1][n-1]==1) { return 0; }

    var dp = Array.from(new Array(m).fill(0), () => new Array(n).fill(0));
    // 这里不需要反过来考虑，如果第一列中间有一个石头，则石头下面的永远也走不到终点，石头上面的还有一次机会
    for (var i=0; i<m; i++) {
        if (obstacleGrid[i][0] != 1) { dp[i][0] = 1; }
        else { break; }
    }
    for (var j=0; j<n; j++) {
        if (obstacleGrid[0][j] != 1) { dp[0][j] = 1; }
        else { break; }
    }
    for (var i=1; i<m; i++) {
        for (var j=1; j<n; j++) {
            if (obstacleGrid[i][j] != 1) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
    }
    return dp[m-1][n-1];
};
// @lc code=end

