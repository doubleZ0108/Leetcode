/*
 * @lc app=leetcode.cn id=13 lang=javascript
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var T = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000,
    }
    var res = 0;
    var i=0;
    while (i<s.length) {
        if ((i+1 < s.length) &&
            (s[i] == "I" && (s[i+1]=="V" || s[i+1]=="X")) ||
            (s[i] == "X" && (s[i+1]=="L" || s[i+1]=="C")) ||
            (s[i] == "C" && (s[i+1]=="D" || s[i+1]=="M")) ) {
            res += T[s[i+1]] - T[s[i]];
            i += 2;
        } else {
            res += T[s[i]];
            i++;
        }
    }
    return res;
};
// @lc code=end

