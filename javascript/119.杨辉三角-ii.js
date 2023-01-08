/*
 * @lc app=leetcode.cn id=119 lang=javascript
 *
 * [119] 杨辉三角 II
 */

// @lc code=start
/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    if (rowIndex == 0) { return [1]; }
    var queue = [1, 1];
    for (var i=2; i<=rowIndex; i++) {
        queue.push(1);
        var last = queue.shift();
        for (var j=1; j<i; j++) {
            var tmp = queue.shift();
            queue.push(last + tmp);
            last = tmp;
        }
        queue.push(1);
    }
    return queue;
};
// @lc code=end

