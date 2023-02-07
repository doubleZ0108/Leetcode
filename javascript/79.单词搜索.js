/*
 * @lc app=leetcode.cn id=79 lang=javascript
 *
 * [79] 单词搜索
 * 
 * 解法1(T25% S76%)：又是一道有趣的深搜问题，但比普通的搜索要难一点，首先每一位的字母都不一样且要和word对应位相同（之前一般都是1围成的岛屿这样相同的元素），因此DFS要多添加一个index位，其次每位不能重复，也就意味着如果某一次是往右一位，下次就不能再往左回来了既是这位字母和idx+2相同，因此需要引入visited数组记录哪里已经走过了。有一个点之前没遇到过，就是可能递归的过程中发现多个方向都有相同字符，到底匹配哪个才能达到全局最优解，因此如果某个方向没有最终解，要把它的visited值变回false。主循环就很简单了，如果第一个字符匹配，那么就从这里开始深搜。
 */

// @lc code=start
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    var visited = Array.from(new Array(board.length), () => new Array(board[0].length).fill(false));
    var deepin = function(x, y, i) {
        if (x<0 || y<0 || x>board.length-1 || y>board[0].length-1 || board[x][y]!=word[i] || visited[x][y]) {
            return false;
        }
        if (i==word.length-1) {
            return true;
        }
        visited[x][y] = true;
        if (deepin(x+1, y, i+1) || deepin(x-1, y, i+1) || deepin(x, y+1, i+1) || deepin(x, y-1, i+1)) {
            return true;
        } else {
            visited[x][y] = false;
            return false;
        }
    };

    for (var i=0; i<board.length; i++) {
        for (var j=0; j<board[i].length; j++) {
            if (board[i][j] == word[0]) {
                visited = Array.from(new Array(board.length), () => new Array(board[0].length).fill(false));
                var res = deepin(i, j, 0);
                if (res) {
                    return true;
                }
            }
        }
    }
    return false;
};
// @lc code=end

