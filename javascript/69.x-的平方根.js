/*
 * @lc app=leetcode.cn id=69 lang=javascript
 *
 * [69] x 的平方根 
 * 
 * 我们是想求解 t^2 = x 的解t0
 * 设 f(t) = t^2 - x，也就是要求 f(t)=0的解t0
 * 根据泰勒公式: f(x) = f(x0) + f'(x)(x-x0)/1!
 * 有 f(t) = t0^2 - x + 2t0(t-t0)，另展开的 f(t) = 0
 * 整理可得 t = (t0^2 + x) / (2*t0)
 * 把上式看成递推公式，也就是如果我们想求x的平方根，只需要根据这个公式不停迭代就可以不断精细的求接触平方根t
 * 因为本题只考虑整数位，因此终止条件是t^2比x小或者相等，因为t是从一个很大的数开始试，因此如果t^2比x小了，那就意味着这个转折点正好就是x的平方根的整数位
 */

// @lc code=start
/**
 * @param {number} x
 * @return {number}
 */
// 简单二分查找法
var mySqrt = function(x) {
    if (x<=1) { return x; }

    var i=1, j=Math.floor(x/2);
    while (i <= j) {
        var mid = Math.floor((i+j)/2);

        if ((mid*mid==x) || (mid*mid<x && (mid+1)*(mid+1)>x)) {
            return mid;
        }

        if (mid * mid > x) {
            j = mid-1;
        } else if (mid * mid < x) {
            i = mid+1;
        }
    }
};

// ！牛顿迭代法
var mySqrt2 = function(x) {
    if (x<=1) { return x; }

    var t = Math.floor(x / 2);
    while (t*t > x) {
        t = Math.floor((t*t + x) / (2*t));
    }
    return t;
};
// @lc code=end

