/*
 * @lc app=leetcode.cn id=130 lang=javascript
 *
 * [130] 被围绕的区域
 * 
 * 解法1(T44% S44%)：所有与边上O相邻的O都不会被修改，其他的O都修改，那不妨先通过DFS找到所有与边上O相连的O，将这些O先变为Z，这样那些要被修改成X的O就暴露出来了，一次遍历，将仍然能是O的变为X，将变为Z的变回O
 */

// @lc code=start
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    var deepin = function(x, y) {
        if (x<0 || y<0 || x>board.length-1 || y>board[0].length-1 || board[x][y]!='O') {
            return;
        }
        board[x][y] = 'Z';
        deepin(x+1, y);
        deepin(x, y+1);
        deepin(x-1, y);
        deepin(x, y-1);
    };

    for (var j=0; j<board[0].length; j++) {
        if (board[0][j] == 'O') {
            deepin(0, j);
        }
        if (board[board.length-1][j] == 'O') {
            deepin(board.length-1, j);
        }
    }
    for (var i=1; i<board.length-1; i++) {
        if (board[i][0] == 'O') {
            deepin(i, 0);
        }
        if (board[i][board[0].length-1] == 'O') {
            deepin(i, board[0].length-1);
        }
    }

    for (var i=0; i<board.length; i++) {
        for (var j=0; j<board[i].length; j++) {
            if (board[i][j] == 'O') {
                board[i][j] = 'X';
            } else if (board[i][j] == 'Z') {
                board[i][j] = 'O';
            }
        }
    }
};
// @lc code=end

