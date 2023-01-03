/*
 * @lc app=leetcode.cn id=48 lang=javascript
 *
 * [48] 旋转图像
 * 
 * 当看到有些数量是很小并且是确定的，可以直接写，不要再用一重循环了
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    var N = matrix.length;
    for (var loop=0; loop<Math.floor(N/2); loop++) {
        for (var i=0; i<N-(2*loop)-1; i++) {
            var tmp = matrix[loop][loop+i];
            matrix[loop][loop+i] = matrix[N-1-loop-i][loop];
            matrix[N-1-loop-i][loop] = matrix[N-1-loop][N-1-loop-i];
            matrix[N-1-loop][N-1-loop-i] = matrix[loop+i][N-1-loop];
            matrix[loop+i][N-1-loop] = tmp;
        }
    }
};
// @lc code=end

