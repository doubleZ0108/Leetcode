/*
 * @lc app=leetcode.cn id=55 lang=javascript
 *
 * [55] 跳跃游戏
 * 
 * 解法1(JS T14% S19%)：动态规划，设置一维dp数组初始化为false，代表每个位置都不可以到达，从0号开始，将其置为true，然后根据nums[i]的范围将这些位置的dp都置为true，如果能将最后一位的dp位变为true则代表可以到达
    很明显，这种方法做了很多重复的染色
 *
 * 解法2(超时 75/170)：递归，根据每个位置能往前跳的步数依次递归
 * 
 * 解法3(T65% S58%)：贪心，解法1太保守了因为一个一个位置往后试探，我们可以直接试探当前位置能到达的最远位置rightmost，如果最远位置超过了数组长度那肯定能到到达最后一位，但是有一个特殊情况，如果当前遍历的idx比我们不断更新的rightmost还大，就意味着我们上一步跳不到这，也就意味着这里就是我能跳的最远位置了，此时直接返回false，如果没有特殊情况的话不断更新rightmost为当前能跳的最远位置即可
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
// 解法3 贪心
var canJump = function(nums) {
    var rightmost = 0;
    for (var i=0; i<nums.length; i++) {
        if (rightmost >= nums.length-1) {
            return true;
        }
        if (i > rightmost) {
            return false;
        }
        rightmost = Math.max(rightmost, i+nums[i]);
    }
    return false;
};


// 解法1 动态规划
var canJump1 = function(nums) {
    var dp = new Array(nums.length).fill(false);
    dp[0] = true;
    for (var i=0; i<nums.length; i++) {
        if (dp[i]) {
            for (var j=i; j<nums.length && j<i+nums[i]+1; j++) {
                dp[j] = true;

                if (dp[nums.length-1]) {
                    return true;
                }
            }
        }
    }
    return dp[nums.length-1];
};

// 解法2 超时
var canJump2 = function(nums) {
    var deepin = function(idx) {
        if (idx == nums.length-1) {
            return true;
        }
        for (var i=idx+1; i<idx+nums[idx]+1; i++) {
            if (deepin(i)) {
                return true;
            }
        }
        return false;
    };
    return deepin(0);
};
// @lc code=end

