/*
 * @lc app=leetcode.cn id=50 lang=java
 *
 * [50] Pow(x, n)
 *
 * Java要注意，-2147483648没超过int的范围，但是把它变成整数2147483648就超过了int的范围，所以一上来判断幂次是否为正数会直接报错，或直接从最大值变成0溢出了
 */

// @lc code=start
class Solution {
    public double myPow(double x, long n) {
        if (n == 0) { return 1; }
        if (n < 0) { return 1. / myPow(x, -n); }
        if (n % 2 == 1) {
            return x * myPow(x, n-1);
        } else {
            double tmp = 0.0;
            tmp = myPow(x, (int) (n/2));
            return tmp * tmp;
        }
    }

    public double myPow2(double x, long n) {
        double res = 1.0;
        boolean flag = false;
        if (n < 0) {
            flag = true;
            n = -n;
        }
        while (n != 0) {
            if (n % 2 == 1) {
                res *= x;
            }
            x *= x;
            n /= 2;
        }
        if (flag) { res = 1. / res; }
        return res;
    }
}
// @lc code=end

