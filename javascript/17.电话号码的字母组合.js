/*
 * @lc app=leetcode.cn id=17 lang=javascript
 *
 * [17] 电话号码的字母组合
 * 
 * 回溯
 */

// @lc code=start
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    var res = [];
    var T = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];

    if (digits.length == 0) { return []; }
    else if (digits.length == 1) { return T[digits[0]].split(""); }

    var callCombinations = function(part, idx) {
        if (part.length == digits.length) {
            res.push(part);
            return;
        }
        var pos = parseInt(digits[idx]);
        for (var i=0; i<T[pos].length; i++) {
            callCombinations(part + T[pos][i], idx+1);
        }
    };
    callCombinations("", 0);

    return res;
};
// @lc code=end

