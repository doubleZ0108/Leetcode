/*
 * @lc app=leetcode.cn id=125 lang=javascript
 *
 * [125] 验证回文串
 */

// @lc code=start
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    var isNum = function(ch) {
        if (ch>='0' && ch<='9') { return true; }
        else { return false; }
    }
    var isAlpha = function(ch) {
        if ((ch>='a' && ch<='z') || (ch>='A' && ch<='Z')) { return true; }
        else { return false; }
    }
    
    var isPalindrome = function(s) {
        var i=0, j=s.length-1;
        while (i<j) {
            while ((i<j) && !(isNum(s[i]) || isAlpha(s[i]))) { i++; }
            while ((i<j) && !(isNum(s[j]) || isAlpha(s[j]))) { j--; }
            if (i>=j) { break; }
    
            if (isNum(s[i]) && isNum(s[j]) && s[i]==s[j]) {
                i++;
                j--;
            } else if (isAlpha(s[i]) && isAlpha(s[j]) && s[i].toLowerCase()==s[j].toLowerCase()) {
                i++;
                j--;
            } else {
                return false;
            }
        }
        return true;
    };
};
// @lc code=end

