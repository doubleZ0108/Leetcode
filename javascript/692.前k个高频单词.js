/*
 * @lc app=leetcode.cn id=692 lang=javascript
 *
 * [692] 前K个高频单词
 * 
 * 多个排序准则，排序两次就好，先按照第二要求排，再按照第一要求排
 */

// @lc code=start
/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function(words, k) {
    var freq = new Map();
    for (var word of words) {
        if (!freq.has(word)) {
            freq.set(word, 1);
        } else {
            freq.set(word, freq.get(word)+1);
        }
    }
    var freqarr = [...freq.entries()].sort();
    freqarr.sort((a, b) => b[1]-a[1])
    return freqarr.slice(0, k).map(x => x[0]);
};
// @lc code=end

