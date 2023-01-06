/*
 * @lc app=leetcode.cn id=118 lang=javascript
 *
 * [118] 杨辉三角
 */

// @lc code=start
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    var res = [[1], [1, 1]];
    if (numRows==1) { return [[1]]; }
    else if (numRows==2) { return res; }

    for (var i=2; i<numRows; i++) {
        var row = [1];
        for (var j=1; j<res[i-1].length; j++) {
            row.push(res[i-1][j-1] + res[i-1][j]);
        }
        row.push(1);

        res.push(row);
    }
    return res;
};
// @lc code=end

