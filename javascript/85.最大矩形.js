/*
 * @lc app=leetcode.cn id=85 lang=javascript
 *
 * [85] 最大矩形
 * 
 * 写的时候没遇到什么卡，但题目本身还是十分有趣的
 */

// @lc code=start
/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {
    if (matrix.length == 0) { return 0; }
    var rows = matrix.length, cols = matrix[0].length;
    var dp_top = Array.from(new Array(rows).fill(0), ()=>new Array(cols).fill(0));
    for (var j=0; j<cols; j++) {
        if (matrix[0][j] == "1") {
            dp_top[0][j] = 1;
        }
        for (var i=1; i<rows; i++) {
            if (matrix[i][j] == "1") {
                dp_top[i][j] = dp_top[i-1][j]+1;
            }
        }
    }

    var maxArea = 0;
    for (var i=0; i<rows; i++) {
        for (var j=0; j<cols; j++) {
            if (matrix[i][j] == "1") {
                var minHeight = dp_top[i][j];
                for (var left=j; left>=0 && matrix[i][left] == "1"; left--) {
                    minHeight = Math.min(minHeight, dp_top[i][left]);
                    maxArea = Math.max(maxArea, minHeight * (j-left+1));
                }
            }
        }
    }

    return maxArea;
};
// @lc code=end

