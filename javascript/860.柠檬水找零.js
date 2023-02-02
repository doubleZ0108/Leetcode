/*
 * @lc app=leetcode.cn id=860 lang=javascript
 *
 * [860] 柠檬水找零
 * 
 * 解法1(JS T14% S31%)：因为钱只有三种，因此直接暴力即可，因为需要频繁读写每种钱的数量，因此通过哈希表来维护三种钱的个数（JS好像一用哈希表就很慢orz）；如果是5块那就直接存进来没其他事；如果是10块，当前我有5块的那就能找零，多一张10块少一张5块；如果是20有两种组合可能，找10+5块或5+5+5块，注意要先尽可能多的找10块出去。将以上逻辑通过if-else写完即可
 */

// @lc code=start
/**
 * @param {number[]} bills
 * @return {boolean}
 */
var lemonadeChange = function(bills) {
    var mine = {5: 0, 10: 0, 20: 0};
    for (var bill of bills) {
        if (bill == 5) {
            mine[5]++;
        } else if (bill == 10) {
            if (mine[5] > 0) {
                mine[5]--;
                mine[10]++;
            } else {
                return false;
            }
        } else {
            if (mine[10]>0 && mine[5]>0) {
                mine[20]++;
                mine[10]--;
                mine[5]--;
            } else if (mine[5]>=3) {
                mine[20]++;
                mine[5] -= 3;
            } else {
                return false;
            }
        }
    }
    return true;
};
// @lc code=end

