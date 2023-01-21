/*
 * @lc app=leetcode.cn id=934 lang=javascript
 *
 * [934] 最短的桥
 * 
 * 注意啥叫dfs啥叫bfs：
 *  bfs是找到一个解就可以了，第一个岛向外延伸只要碰到第二个岛就停，这就叫bfs
 *  dfs是找到所有解，把第一个岛所有都标为2这就是dfs
 * 
 * 注意js用set查找会超时，只能变成二维bit数组
 * 把所有可能起始点都直接放在queue中做会更快，每个点单独做完再取最小值浪费了很多计算
 */

// @lc code=start
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestBridge = function(grid) {
    var n = grid.length;
    var nodes = [];

    var dfs = function(i, j) {
        if (i<0 || i>=n || j<0 || j>=n) { return; }
        if (grid[i][j]==0 || grid[i][j]==2) { return; }

        grid[i][j] = 2;
        nodes.push([i, j]);
        dfs(i+1, j);
        dfs(i-1, j);
        dfs(i, j+1);
        dfs(i, j-1);
    };

    var bfs = function(i, j) {
        var queue = [];
        var visited = Array.from(new Array(n), ()=>new Array(n).fill(false));
        for (var node of nodes) {
            queue.push([node[0], node[1], 0]);
            visited[node[0]][node[1]] = true;
        }
        
        while (queue.length) {
            var data = queue.shift();
            var x=data[0], y=data[1], cost=data[2];
            if (grid[x][y] == 1) {
                return cost-1;
            }
            for (var dir of [[x+1,y], [x-1,y], [x,y-1], [x,y+1]]) {
                var dx=dir[0], dy=dir[1];
                if (dx>-1 && dx<n && dy>-1 && dy<n && !visited[dx][dy]) {
                    queue.push([dx, dy, cost+1]);
                    visited[dx][dy] = true;
                }
            }
        }
    };


    for (var i=0; i<n; i++) {
        for (var j=0; j<n; j++) {
            if (grid[i][j] == 1) {
                dfs(i, j);

                return bfs();
            }
        }
    }
};
// @lc code=end

