/*
 * @lc app=leetcode.cn id=11 lang=javascript
 *
 * [11] 盛最多水的容器
 * 
 * 很有趣的一道题，只需要想明白一件事，最大的水池面积无非是左面一个挡板和右面一个挡板围起来的面积，所以只需要拿着两个挡板从最左和最右出发，如果往里走一步挡板还变小了那肯定面积会变小，因此根据短板效应，哪个挡板短哪边就往里试图找到一个更长的板（只有这样面积才可能变大）
 */

// @lc code=start
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var res = 0;
    var i=0, j=height.length-1;
    while (i < j) {
        res = Math.max(res, (j-i) * Math.min(height[i], height[j]));
        if (height[i] < height[j]) { i++; }
        else { j--; }
    }
    return res;
};


// 双重循环 超时
// var maxArea1 = function(height) {
//     var area = new Array(height.length).fill(0)
//     for (var i=0; i<height.length; i++) {
//         var thismax = 0;
//         for (var j=i+1; j<height.length; j++) {
//             thismax = Math.max(thismax, (j-i)*Math.min(height[i], height[j]));
//         }
//         area[i] = thismax;
//     }
//     return Math.max(...area);
// };
// @lc code=end

