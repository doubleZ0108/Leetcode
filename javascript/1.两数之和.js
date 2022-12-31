/*
 * @lc app=leetcode.cn id=1 lang=javascript
 *
 * [1] 两数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // 解法1: 双重循环
    for (var i=0; i<nums.length; i++) {
        for (var j=i+1; j<nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j];
            }
        }
    }
};

var twoSum2 = function(nums, target) {
    // 解法2: 数组切片 + find
    for (var i=0; i<nums.length; i++) {
        var remains = nums.slice(i+1);
        var index = remains.findIndex((element) => element + nums[i] == target)
        if (index != -1) {
            return [i, i+index+1]
        }
    }
};

var twoSum3 = function(nums, target) {
    // 解法3: 先排序，二分查找，再原数组一次遍历提取下标
    var nums_ = nums.concat()
    nums_.sort((a, b) => a - b);

    for (var i=0, j=nums.length-1; i<nums.length && j>-1; ) {
        if (nums_[i] + nums_[j] > target) {
            j--;
        } else if (nums_[i] + nums_[j] < target) {
            i++;
        } else {
            break;
        }
    }

    var res = [];
    for (var a=0; a<nums.length; a++) {
        if (nums[a] == nums_[i] || nums[a] == nums_[j]) {
            res.push(a);
        }
    }

    return res;
};
// @lc code=end

