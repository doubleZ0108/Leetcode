/*
 * @lc app=leetcode.cn id=412 lang=javascript
 *
 * [412] Fizz Buzz
 * 
 * 解法1(T76% S68%)：没啥好说的，这题主要考if的逻辑判断，第一个条件设为 && 之后后面的else直接就排除了这种选项，总的来说是if可以帮你排出很多情况
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    var res = [];
    for (var i=1; i<=n; i++) {
        if (i%3==0 && i%5==0) {
            res.push("FizzBuzz");
        } else if (i%3==0) {
            res.push("Fizz");
        } else if (i%5==0) {
            res.push("Buzz");
        } else {
            res.push(i.toString());
        }
    }
    return res;
};
// @lc code=end

