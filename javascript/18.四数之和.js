/*
 * @lc app=leetcode.cn id=18 lang=javascript
 *
 * [18] 四数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    nums = nums.sort((a, b) => a-b);
    var res = [];
    var visited = [];
    for (var i=0; i<nums.length-3; ++i) {
        for (var j=i+1; j<nums.length-2; ++j) {
            var p=j+1, q=nums.length-1;
            while (p < q) {
                var tmp = [nums[i], nums[j], nums[p], nums[q]];
                var total = _.sum(tmp);
                if (total == target) {
                    if (!visited.includes(tmp.toString())) {
                        res.push(tmp);
                        visited.push(tmp.toString());
                    }
                    ++p;
                    --q;
                } else if (total < target) {
                    ++p;
                } else {
                    --q;
                }
            }
        }
    }
    return res;
};
// @lc code=end

