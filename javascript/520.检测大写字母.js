/*
 * @lc app=leetcode.cn id=520 lang=javascript
 *
 * [520] 检测大写字母
 */

// @lc code=start
/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    var flag = true;
    for (var ch of word) {
        if (!(ch>='A' && ch<='Z')) {
            flag = false;
            break;
        }
    }
    if (flag) { return true; }

    flag = true;
    for (var ch of word) {
        if (!(ch>='a' && ch<='z')) {
            flag = false;
            break;
        }
    }
    if (flag) { return true; }

    flag = true;
    if (word[0]>='A' && word[0]<='Z') {
        for (var i=1; i<word.length; i++) {
            if (!(word[i]>='a' && word[i]<='z')) {
                flag = false;
                break;
            }
        }
    } else {
        flag = false;
    }

    if (flag) { return true; }
    return false;
};
// @lc code=end

