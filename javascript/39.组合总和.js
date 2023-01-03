/*
 * @lc app=leetcode.cn id=39 lang=javascript
 *
 * [39] 组合总和
 */

// @lc code=start
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    candidates.sort((a,b)=>(a-b));
    var res = [];
    var combine = function(parts, remain) {
        if (remain < 0) { return; }
        else if (remain == 0) { 
            res.push(parts);
            return;
        }
        for (var i in candidates) {
            if (parts.length==0 || candidates[i] >= parts[parts.length-1]) {
                // 要注意回溯这里必须直接在函数调用内部实现内容变更，如果把添加元素直接写成parts.push(x)在外面+调用之后再pop()，则内容都会为空
                combine(parts.concat(candidates[i]), remain-candidates[i]);
            }
        }
    };
    combine([], target);
    return res;
};
// @lc code=end

