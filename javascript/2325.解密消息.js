/*
 * @lc app=leetcode.cn id=2185 lang=javascript
 *
 * [2325] 解密消息
 * 
 * 解法1(T42% S89%)：非常经典的哈希表结构，首先遍历key，将每个非空格不重复字符串与abcde建立关系，然后再一遍遍历message进行转换
 *   - js中字符串偏移：`String.fromCharCode('a'.charCodeAt(0) + idx)`
 *   - py：`chr(ord('a') + idx)`
 */

// @lc code=start
/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */
var decodeMessage = function(key, message) {
    var table = new Map();
    var baseidx = 0;
    for (var ch of key) {
        if (ch != " " && !table.has(ch)) {
            table.set(ch, String.fromCharCode('a'.charCodeAt(0) + baseidx));
            baseidx++;
        }
    }

    var res = "";
    for (var ch of message) {
        if (ch != " ") {
            res += table.get(ch);
        } else {
            res += " ";
        }
    }
    return res;
};
// @lc code=end