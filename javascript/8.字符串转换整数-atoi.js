/*
 * @lc app=leetcode.cn id=8 lang=javascript
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    if (s.length == 0) { return 0; }

    s = s.trimStart();
    switch (s[0]) {
        case "-":
            var flag = true;
            s = s.slice(1);
            break;
        case "+":
            var flag = false;
            s = s.slice(1);
            break;
        case "0": case "1": case "2":case "3": case "4": case "5":case "6": case "7": case "8": case "9":
            var flag = false;
            break;
        default:
            return 0;
    }

    var i=0;
    while (i<s.length && (s[i]>="0" && s[i]<="9")) { i++; }
    if (i==0) { return 0; }     // 如果第一个有用字符就非法

    var res = parseInt(s.slice(0, i));
    if (flag) { res = -res; }
    if (res < -Math.pow(2, 31)) { return -Math.pow(2, 31); }
    else if (res > Math.pow(2, 31)-1) { return Math.pow(2, 31)-1; }
    return res;
};
// @lc code=end

