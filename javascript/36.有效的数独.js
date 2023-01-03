/*
 * @lc app=leetcode.cn id=36 lang=javascript
 *
 * [36] 有效的数独
 * 
 * 解法1(T86% S71%): 思路是很传统的，分三种情况，首先一行一行，再一列一列看，最后看9个3x3格子中是否有重复。怎么看是否有重复呢？通过一个长度为9的一维bits数组来判断，如果某位被第二次标记则直接返回false，注意每一组都要清空这个bits数组。唯一有点难度的是如何优雅的写9个3x3格子的遍历，只需要确定左上角下标即可，确定了左上角就只需要横着竖着都遍历3个位置即可，而对于左上角下标的确定，通过一个取余运算就可以实现，唯一要注意的是，当j重新到达了0边界后，i才需要移动，如果i和j同时取余移动，则只遍历了对角线上的3个3x3格子，会导致很多地方没看到
 */

// @lc code=start
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    var N = 9;
    for (var i=0; i<N; i++) {
        var bits = new Array(N).fill(0);
        for (var j=0; j<N; j++) {
            if (board[i][j] != '.') {
                bits[board[i][j] - '1']++;
                if (bits[board[i][j]-'1'] > 1) { return false; }
            }
        }
    }
    for (var j=0; j<N; j++) {
        var bits = new Array(N).fill(0);
        for (var i=0; i<N; i++) {
            if (board[i][j] != '.') {
                bits[board[i][j] - '1']++;
                if (bits[board[i][j]-'1'] > 1) { return false; }
            }
        }
    }
    var i=0, j=0;
    for (var num=0; num<N; num++) {
        var bits = new Array(N).fill(0);
        for (var ii=i; ii<i+3; ii++) {
            for (var jj=j; jj<j+3; jj++) {
                if (board[ii][jj] != '.') {
                    bits[board[ii][jj]-'1']++;
                    if (bits[board[ii][jj]-'1'] > 1) { return false; }
                }
            }
        }
        j = (j+3) % N;
        if (j == 0) {   // 注意这里，如果不加这个if，则只走了对角线三个3x3格子，正确的应该是横着走完3个3x3格子再往下走
            i = (i+3) % N;
        }
    }
    return true;
};
// @lc code=end

