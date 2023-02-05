/*
 * @lc app=leetcode.cn id=383 lang=javascript
 *
 * [383] 赎金信
 * 
 * 解法1(T65% S77%)：首先用哈希表统计magazine中每个字符出现的频次，然后对于note的每个字符在哈希表中递减，如果哈希表中找不到该字符或是数量已经减没了则false
 *   JS的Map注意还是通过要通过`set()`和`get()`使用，像python直接用数组的形式访问会有问题
 */

// @lc code=start
/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    var table = new Map();
    for (var s of magazine) {
        if (!table.has(s)) {
            table.set(s, 1);
        } else {
            table.set(s, table.get(s)+1);
        }
    }

    for (var s of ransomNote) {
        if (!table.has(s) || table.get(s)<=0) {
            return false;
        } else {
            table.set(s, table.get(s)-1);
        }
    }
    return true;
};
// @lc code=end

