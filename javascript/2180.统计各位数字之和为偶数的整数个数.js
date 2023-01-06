/*
 * @lc app=leetcode.cn id=2180 lang=javascript
 *
 * [2180] 统计各位数字之和为偶数的整数个数
 * 
 * 解法1(T94% S85%): 就没啥好说的，总归是要把所有数字都看一遍才知道有多少个的，对于每个数字的判断就是经典的while(num)不断取余和整除10即可 
 */

// @lc code=start
/**
 * @param {number} num
 * @return {number}
 */
var countEven = function(num) {
    var res = 0;
    for (var i=1; i<=num; i++) {
        var d = i;
        var tmp = 0;
        while (d) {
            tmp += d % 10;
            d = Math.floor(d / 10);
        }
        if (tmp % 2 == 0) {
            res++;
        }
    }
    return res;
};
// @lc code=end

