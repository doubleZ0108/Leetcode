/*
 * @lc app=leetcode.cn id=500 lang=javascript
 *
 * [500] 键盘行
 * 
 * 题不难，但代码还是很绕的，想好一种解决办法就去实现，不要在一套代码里出现两种解决思路，会混乱的
 */

// @lc code=start
/**
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(words) {
    var sets = [new Set("qwertyuiop".split("")), new Set("asdfghjkl".split("")), new Set("zxcvbnm".split(""))];

    var res = [];
    for (var word of words) {
        var i=0;
        for (; i<sets.length; i++) {
            if (sets[i].has(word[0].toLowerCase())) {
                break;
            }
        }
        var flag = true;
        for (var j=1; j<word.length; j++) {
            if (!sets[i].has(word[j].toLowerCase())) {
                flag = false;
                break;
            }
        }

        if (flag) {
            res.push(word);
        }
    }
    return res;
};
// @lc code=end

