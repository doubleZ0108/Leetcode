/*
 * @lc app=leetcode.cn id=2042 lang=javascript
 *
 * [2042] 检查句子中的数字是否递增
 * 
 * 解法1(T80% S64%): 非常简单标准的一道数组处理题，借用`split()`可以很方便的把字符串分割成tokens数组，由于题目描述的非常普通甚至没啥特殊情况，因此不需要一位一位的判断，直接判断每个token第一位是不是数字字符，然后通过一个变量判断是否严格递增即可
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

