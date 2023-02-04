/*
 * @lc app=leetcode.cn id=733 lang=javascript
 *
 * [733] 图像渲染
 * 
 * 解法1(T43% S63%)：首先保存并判断初始位置的颜色，如果填充颜色跟初始颜色相同就不用做了。深度优先搜索，将上下左右四个位置不断递归。
 * 解法2(T43% S22%)：光度优先搜索，通过队列维护坐标，每次将四个方向中合理的位置压队
 */

// @lc code=start
/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
// 解法1
var floodFill = function(image, sr, sc, color) {
    var base = image[sr][sc];
    if (base == color) {
        return image;
    }

    var deepin = function(x, y) {
        if (x<0 || x>=image.length || y<0 || y>=image[0].length || image[x][y]!=base) {
            return;
        }
        image[x][y] = color;
        deepin(x+1, y);
        deepin(x-1, y);
        deepin(x, y+1);
        deepin(x, y-1);
    };
    deepin(sr, sc);
    return image;
};

// 解法2
var floodFill2 = function(image, sr, sc, color) {
    var base = image[sr][sc];
    if (base == color) {
        return image;
    }

    var queue = [[sr, sc]];
    while (queue.length) {
        var data = queue.shift();
        var x=data[0], y=data[1];
        image[x][y] = color;
        for (var delta of [[-1, 0], [0, -1], [1, 0], [0, 1]]) {
            var dx=x+delta[0], dy=y+delta[1];
            if (dx<0 || dx>=image.length || dy<0 || dy>=image[0].length || image[dx][dy]!=base) {
                continue;
            }
            queue.push([dx, dy]);
        }
    }
    return image;
};
// @lc code=end

