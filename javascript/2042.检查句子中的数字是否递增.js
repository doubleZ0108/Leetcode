/*
 * @lc app=leetcode.cn id=2042 lang=javascript
 *
 * [2042] 检查句子中的数字是否递增
 */

// @lc code=start
/**
 * @param {string} s
 * @return {boolean}
 */
var areNumbersAscending = function(s) {
    var tokens = s.split(" ");
    var num = 0;
    for (var i in tokens) {
        if (tokens[i][0] >= "1" && tokens[i][0] <= "9") {
            var tmp = parseInt(tokens[i]);
            if (tmp > num) { num = tmp; }
            else { return false; }
        }
    }
    return true;
};
// @lc code=end

