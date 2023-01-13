/*
 * @lc app=leetcode.cn id=240 lang=javascript
 *
 * [240] 搜索二维矩阵 II
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    var m = matrix.length, n = matrix[0].length;
    var i=0, j=n-1;
    while (i<m && j>-1) {
        if (matrix[i][j] == target) {
            return true;
        } else if (target < matrix[i][j]) {
            j--;
        } else {
            i++;
        }
    }
    return false;
};
// @lc code=end

