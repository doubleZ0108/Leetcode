/*
 * @lc app=leetcode.cn id=64 lang=javascript
 *
 * [64] 最小路径和
 */

// @lc code=start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    var m = grid.length, n = grid[0].length;
    for (var i=1; i<m; i++) {
        grid[i][0] += grid[i-1][0];
    }
    for (var j=1; j<n; j++) {
        grid[0][j] += grid[0][j-1];
    }
    for (var i=1; i<m; i++) {
        for (var j=1; j<n; j++) {
            grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
        }
    }
    return grid[m-1][n-1];
};
// @lc code=end

