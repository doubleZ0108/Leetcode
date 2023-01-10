/*
 * @lc app=leetcode.cn id=374 lang=javascript
 *
 * [374] 猜数字大小
 */

// @lc code=start
/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function(n) {
    var i=1, j=n;
    while (i<j) {
        var mid = Math.floor((i+j)/2);
        var t = guess(mid);
        if (t == 0) {
            return mid;
        } else if (t == -1) {
            j = mid - 1;
        } else {
            i = mid + 1;
        }
    }
    return i;
};
// @lc code=end

