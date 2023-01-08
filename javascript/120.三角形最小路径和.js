/*
 * @lc app=leetcode.cn id=120 lang=javascript
 *
 * [120] 三角形最小路径和
 */

// @lc code=start
/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    for (var i=1; i<triangle.length; i++) {
        for (var j=0; j<triangle[i].length; j++) {
            if (j==0) {
                triangle[i][j] += triangle[i-1][0]
            } else if (j==triangle[i].length-1) {
                triangle[i][j] += triangle[i-1][triangle[i-1].length-1];
            } else {
                triangle[i][j] += Math.min(triangle[i-1][j-1], triangle[i-1][j]);
            }
        }
    }
    return Math.min(...triangle[triangle.length-1]);
};
// @lc code=end

