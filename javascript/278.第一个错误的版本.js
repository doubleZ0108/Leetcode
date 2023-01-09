/*
 * @lc app=leetcode.cn id=278 lang=javascript
 *
 * [278] 第一个错误的版本
 */

// @lc code=start
/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        var i=1, j=n;
        while (i<j) {
            var mid = Math.floor((i+j)/2);
            if (isBadVersion(mid)) {
                j = mid-1;
            } else {
                i = mid+1;
            }
        }
        return isBadVersion(i) ? i : i+1;
    };
};
// @lc code=end

