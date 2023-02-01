/*
 * @lc app=leetcode.cn id=463 lang=javascript
 *
 * [463] 岛屿的周长
 * 
 * 解法1(T62% S35%)：题目还是很有趣的，主要考方向向量的处理，岛屿的周长=每块陆地*4 - 陆地间相邻的边*2，但其实对于每个陆地，只要上下左右看有没有相连陆地，有就减掉1就好，因为计算到那个相邻地地时候还会再减一遍
 */

// @lc code=start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    var res = 0;
    for (var i=0; i<grid.length; i++) {
        for (var j=0; j<grid[i].length; j++) {
            if (grid[i][j] == 1) {
                res += 4
                for (var d of [[-1, 0], [0, -1], [1, 0], [0, 1]]) {
                    var dx=i+d[0], dy=j+d[1];
                    if (dx>-1 && dy>-1 && dx<grid.length && dy<grid[i].length && grid[dx][dy] == 1) {
                        res--;
                    }
                }
            }
        }
    }
    return res;
};
// @lc code=end

