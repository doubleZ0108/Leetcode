/*
 * @lc app=leetcode.cn id=657 lang=javascript
 *
 * [657] 机器人能否返回原点
 * 
 * 解法1(JS T47% S21%)：因为只有四个方向而且还是两两一对，所以问题可以简化为判断UD RL这两对数是否各自相等，通过一个哈希表来统计字符出现频次，并通过&&连接的逻辑判断语句即可
 */

// @lc code=start
/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    var table = {
        'U': 0, 'D': 0,
        'R': 0, 'L': 0,
    };
    for (var move of moves) {
        table[move]++;
    }
    return table['U']==table['D'] && table['R']==table['L'];
};
// @lc code=end

