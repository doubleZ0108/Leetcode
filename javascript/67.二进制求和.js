/*
 * @lc app=leetcode.cn id=67 lang=javascript
 *
 * [67] 二进制求和
 */

// @lc code=start
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    a = a.split("").reverse().map(x => parseInt(x));
    b = b.split("").reverse().map(x => parseInt(x));
    var res = [];
    var bonus = 0;
    var i=0, j=0
    for (; i<a.length && j<b.length; i++, j++) {
        res.push((a[i] + b[j] + bonus) % 2);
        bonus = Math.floor((a[i] + b[j] + bonus) / 2);
    }
    for (; i<a.length; i++) {
        res.push((a[i] + bonus) % 2);
        bonus = Math.floor((a[i] + bonus) / 2);
    }
    for (; j<b.length; j++) {
        res.push((b[j] + bonus) % 2);
        bonus = Math.floor((b[j] + bonus) / 2);
    }
    if (bonus) {
        res.push(bonus);
    }

    return res.reverse().join("");
};

// 大数会计算错误，猜想是精度不够，还是老老实实一位一位自己加
// var addBinary = function(a, b) {
//     var res = parseInt(a, 2) + parseInt(b, 2);
//     return res.toString(2);
// };
// @lc code=end

