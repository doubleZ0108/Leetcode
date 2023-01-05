/*
 * @lc app=leetcode.cn id=78 lang=javascript
 *
 * [78] 子集
 * 
 * 回溯法还是要每一位都做考虑，像这道题输出长度可能不同是不好弄的，所以将输出先用bit字符串表示，例如011就代表nums的第0位不要，第1 2位要，这样就是很标准的回溯法了
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    var res = [];
    var makeSub = function(bitparts, index) {
        if (index == nums.length) {
            var parts = [];
            for (var i in bitparts) {
                if (bitparts[i] == "1") {
                    parts.push(nums[i]);
                }
            }
            res.push(parts);
            return;
        }

        makeSub(bitparts+"0", index+1);
        makeSub(bitparts+"1", index+1);
    };
    makeSub("", 0);
    return res;
};
// @lc code=end

