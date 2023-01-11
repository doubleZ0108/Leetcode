/*
 * @lc app=leetcode.cn id=274 lang=javascript
 *
 * [274] H 指数
 */

// @lc code=start
/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    citations.sort((a,b) => -(a-b));
    for (var i=0; i<citations.length; i++) {
        if (citations[i] < i+1) {
            return i;
        }
    }
    if (citations[citations.length-1] > citations.length+1) {
        return citations.length;
    } else {
        return citations[citations.length-1];
    }
};
// @lc code=end

