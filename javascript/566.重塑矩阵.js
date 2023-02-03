/*
 * @lc app=leetcode.cn id=566 lang=javascript
 *
 * [566] 重塑矩阵
 * 
 * 解法1(T99% S45%)：好久没做过这种二维矩阵的两套下标同时处理的题，蛮有趣的，首先判断维度是否匹配能否转换，因为毕竟要返回一个转换后的矩阵，因此再开一个二维数组也合情合理，一套下标正常for循环，另一套循环通过自增来做，先不断自增j下标，如果j到达边界，则将其重新置为0并自增i下标
 */

// @lc code=start
/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(mat, r, c) {
    if (mat.length * mat[0].length != r*c) {
        return mat;
    }
    var mat_ = Array.from(new Array(r), () => new Array(c));
    var x=0, y=0;
    for (var i=0; i<r; i++) {
        for (var j=0; j<c; j++) {
            mat_[i][j] = mat[x][y];
            y++;
            if (y==mat[0].length) {
                y = 0;
                x++;
            }
        }
    }
    return mat_;
};
// @lc code=end

