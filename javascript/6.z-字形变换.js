/*
 * @lc app=leetcode.cn id=6 lang=javascript
 *
 * [6] Z 字形变换
 */

// @lc code=start
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    // 如果只有1行，i++会数组越界，而且也增加了没必要的循环计算
    if (numRows == 1 || s.length == 1) { return s; }
    
    var T = Array.from(Array(numRows).fill(""), () => new Array(s.length).fill(""));  // 先开一个过长的数组

    var i=0, j=0;
    var flag = "|"
    for (var id=0; id<s.length; id++) {
        T[i][j] = s[id];

        if (flag == "|") { i++; }
        else if (flag == "/") { i--; j++; }

        if (i==numRows-1) { flag = "/"; }
        else if (i==0) {flag = "|"; }
    }
    var maxCol = j+1;

    var res = "";
    for (var i=0; i<numRows; i++) {
        for (var j=0; j<maxCol; j++) {
            if (T[i][j] != "") { res = res.concat(T[i][j]); }
        }
    }
    return res;
};
// @lc code=end

