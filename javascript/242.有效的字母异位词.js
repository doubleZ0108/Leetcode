/*
 * @lc app=leetcode.cn id=242 lang=javascript
 *
 * [242] 有效的字母异位词
 * 
 * js的哈希表非常不优雅
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    var map = new Map();
    for (var ch of s) {
        if (map.has(ch)) {
            map.set(ch, map.get(ch)+1);
        } else {
            map.set(ch, 1);
        }
    }

    for (var ch of t) {
        if (!map.has(ch) || map.get(ch)<=0) {
            return false;
        } else {
            map.set(ch, map.get(ch)-1);
        }
    }
    
    for (var v of map.values()) {
        if (!isNaN(v) && v>0) {
            return false;
        }
    }
    return true;
};
// @lc code=end

