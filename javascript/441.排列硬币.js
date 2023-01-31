/*
 * @lc app=leetcode.cn id=441 lang=javascript
 *
 * [441] 排列硬币
 * 
 * 解法1(T97% S80%)：这题有数学解，设结果为$x$，要满足$x$行所用的硬币比$n$小，而$x+1$行用的硬币比$n$大，根据等差数列有
 * \begin{cases} \frac{(1+x)*x}{2} \le n \\ \frac{(1+x+1)*(x+1)}{2} > n \end{cases}
 * 整理可得
 * \begin{cases} x^2+x-2n \le 0 \\ x^2+3x+2-2n>0 \end{cases}
 * 用求根公式$\frac{-b \pm \sqrt{b^2-4ac}}{2a}$解得入上不等式组
 * \frac{-3 + \sqrt{9-4(2-2n)}}{2} \lt x \le \frac{-1+\sqrt{1+8n}}{2}
 * 其实只需要不等式右边就可以得到本题的解，因为要尽可能多的排列楼梯，只需要对右侧项下取整即可
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function(n) {
    return parseInt((-1 + Math.pow(1+8*n, 0.5))/2);
};
// @lc code=end

