/*
 * @lc app=leetcode.cn id=944 lang=javascript
 *
 * [944] 删列造序
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function(strs) {
    var strs_T = Array.from(new Array(strs[0].length), () => new Array(strs.length));
    for (var i=0; i<strs_T.length; i++) {
        for (var j=0; j<strs_T[0].length; j++) {
            strs_T[i][j] = strs[j][i];
        }
    }
    
    var res = 0;
    for (var i=0; i<strs_T.length; i++) {
        var flag = true;
        for (var j=1; j<strs_T[i].length; j++) {
            if (strs_T[i][j] < strs_T[i][j-1]) {
                flag = false;
                break;
            }
        }
        if (!flag) {
            res++;
        }
    }
    return res;
};
// @lc code=end

