/*
 * @lc app=leetcode.cn id=459 lang=javascript
 *
 * [459] 重复的子字符串
 * 
 * 解法1(T92% S72%)：因为我们并不知道这个被重复的子串有多长，所以只好暴力来做，从长度为1开始，凡是能被原字符串长度整除的都要尝试，对于一个假设的子串长度，首先从0开始切一片作为pattern，然后依次向后匹配整个字符串，如果能一直匹配到结尾那就意味着可以由该子串重复构成
 */

// @lc code=start
/**
 * @param {string} s
 * @return {boolean}
 */
var repeatedSubstringPattern = function(s) {
    for (var base=1; base<=Math.floor(s.length/2); base++) {
        if (s.length % base == 0) {
            var pattern = s.slice(0, base);
            var flag = true;
            for (var i=base; i<s.length; i+=base) {
                if (s.slice(i, i+base) != pattern) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                return true;
            }
        }
    }
    return false;
};
// @lc code=end

