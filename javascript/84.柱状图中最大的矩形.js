/*
 * @lc app=leetcode.cn id=84 lang=javascript
 *
 * [84] 柱状图中最大的矩形
 * 
 * 很快就想到了单调栈，应该就不难了，为什么一直卡住呢，我们再来捋下思路：
 * 维护一个单调栈（存的是下标，因为要求width算面积，只存height宽度就丢了），如果遍历到某元素时发现它比栈顶要小，由于栈底到栈顶递增，所以此时栈顶发现了左边第一个比他小的以及右边第一个比他小的
 * 这样问题就会到了暴力的双重循环法
 * 对于某个元素，如果找到了左边第一个比他小的和右面第一个比他小的，则以当前元素为height的最大面积就可以求解了
 * 
 * 比较坑的是边界的判断，当栈为空，也就意味着左面都比当前元素大，那0就应该是左边界
 * 同样的，如果右面一直比自己大，那找到右边界也还是没有结果，此时添加一个0元素在原数组尾部就可以解决
 */

// @lc code=start
/**
 * @param {number[]} heights
 * @return {number}
 */
// 前后都添加一个0可以更好的处理，因为stack永远不会为空，0总归比所有人都小，左边界一直在那
// 同时需要注意需要while来处理，如果发现一个很小的右边界，它可能是很多人的右边界，在栈里不断的判断是否可以计算
var largestRectangleArea = function(heights) {
    if (heights.length == 1) { return heights[0]; }

    heights.unshift(0);
    heights.push(0);

    var res = 0;
    var stack = [0]; // 单调栈，栈从下到上递增
    for (var i=1; i<heights.length; i++) {
        while (heights[i] < heights[stack[stack.length-1]]) {
            var top = stack.pop();
            res = Math.max(res, heights[top]*(i-stack[stack.length-1]-1))
        }
        stack.push(i);
    }
    
    return res;
};

var largestRectangleArea2 = function(heights) {
    if (heights.length == 1) { return heights[0]; }
    heights.push(0);

    var res = 0;
    var stack = [0]; // 单调栈，栈从下到上递增
    for (var i=1; i<heights.length; i++) {
        while (stack.length && heights[i] < heights[stack[stack.length-1]]) {
            var top = stack.pop();
            if (stack.length!=0) {
                res = Math.max(res, heights[top]*(i-stack[stack.length-1]-1));
            } else {
                res = Math.max(res, heights[top]*(i));
            }
        }
        stack.push(i);
    }
    
    return res;
};

// 超时 95/98 每个位置向左向右找第一个比自己小的，求得最大面积
var largestRectangleArea1 = function(heights) {
    var res = 0;
    for (var i=0; i<heights.length; i++) {
        var left=i-1, right=i+1;
        while (left > -1 && heights[left]>=heights[i]) {
            left--;
        }
        while (right < heights.length && heights[right]>=heights[i]) {
            right++;
        }
        res = Math.max(res, heights[i]*(right-left-1));
    }
    return res;
};
// @lc code=end

