/*
 * @lc app=leetcode.cn id=134 lang=javascript
 *
 * [134] 加油站
 * 
 * 想法是完全正确的，对于失效的条件判断卡了一下
 * oil代表当前油量，每个站点都模拟一下，即加上油减去花费
 * 如果假设通过这个站点导致oil为负，则证明失败，则起始站点设置为i+1并清空油箱重新来
 * 设立一个计数器，如果从某个站点开始能走完所有的站点则找到了结果
 * 如果某次oil为负要重新设立起始站点了，结果发现新要设立的比当前设立的位置还小，那就证明肯定i又走了一圈还没找到解，此时无解
 */

// @lc code=start
/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    var oil = 0;
    var i = 0;
    var res = 0;
    var cnt = 0;
    while (res < gas.length) {
        if (cnt==gas.length) { return res; }

        oil += gas[i] - cost[i];
        if (oil < 0) {
            if (i+1<=res) { break; }
            res = i+1;
            oil = 0;
            cnt = 0;
        } else {
            cnt++;
        }
        i = (i+1)%gas.length;
    }
    return -1;
};
// @lc code=end

