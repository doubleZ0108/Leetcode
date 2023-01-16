/*
 * @lc app=leetcode.cn id=720 lang=javascript
 *
 * [720] 词典中最长的单词
 * 
 * 注意首先要排序，set中的key要一点一点加，不能直接就把原数组加进去，因为可能出现虽然少一位在，但少两位的可能不在，但这并不满足题目要求
 */

// @lc code=start
/**
 * @param {string[]} words
 * @return {string}
 */
var longestWord = function(words) {
    words.sort((a, b) => (a.length-b.length));
    
    var set = new Set([""]);
    var res = "";
    for (var word of words) {
        if (word.length >= res.length && set.has(word.slice(0, word.length-1))) {
            set.add(word);
            if (word.length > res.length || (word.length==res.length && word<res)) {
                res = word;
            }
        }
    }
    return res;
};
// @lc code=end

