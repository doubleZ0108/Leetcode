/*
 * @lc app=leetcode.cn id=139 lang=javascript
 *
 * [139] 单词拆分
 * 
 * 解法1(解答错误)：不断循环wordDict，如果某个word正好是当前s的开头字符，则s从开头裁剪掉该开头继续循环，如果wordDict中所有单词都不是s的开头则结束，但如下例子会提前错误结束
    改进1(超时)：用队列存储中间结果，不要试探完第一个可能的头匹配就break，要尝试所有
    改进2(超时)：不仅做头匹配，也在同一个循环里做尾匹配，这样时间相当于缩短了一半
    改进3：首先先用集合统计两字符串，如果s中有字符没出现在wordDict中则直接返回
 *
 * 解法2(超时 35/45)：还是按照解法1的思路，只不过换成回溯递归实现，这样可以充分遍历所有情况
 *
 * ✨解法3(T41% S59%)：动态规划，看到了超时的样例，发现这样两重循环肯定会超时，考虑到一个长的字符串能否被构成取决于两个短的能否分别被构成，如果可以的话将他们拼起来就可以构成整个字符串。定义dp[i]表示s的前i位能否被字典构成，内部需要另一重循环j来处理，j将长度为i的子串划分为0～j和j～i，0～j能否被构成之前dp[j]已经求结果，因此只需要再看j～i的字符是否在wordDict中，只要找到了一个这样的划分点j，那就是说0～i的串也可以被构成
    注意循环变量起始点和终点
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
// 解法3 动态规划
var wordBreak = function(s, wordDict) {
    var wordset = new Set(wordDict);
    var dp = new Array(s.length+1).fill(false); // 注意这里的长度
    dp[0] = true;
    for (var i=0; i<dp.length; i++) {
        for (var j=0; j<i; j++) {
            if (dp[j] && wordset.has(s.slice(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[dp.length-1];
};

// 解法1 超时
var wordBreak1 = function(s, wordDict) {
    var diff = [...new Set(s.split(""))].filter(x => !new Set(wordDict.join("")).has(x));
    if (diff.length > 0) {
        return false;
    }

    var queue = [s];
    while (queue.length) {
        var remain = queue.shift();
        if (remain == "") {
            return true;
        }
        for (var word of wordDict) {
            if (remain.startsWith(word)) {
                queue.push(remain.slice(word.length, remain.length));
            }
            if (remain.endsWith(word)) {
                queue.push(remain.slice(0, remain.length-word.length));
            }
        }
    }
    return false;
};


// 解法2 超时
var wordBreak = function(s, wordDict) {
    var deepin = function(remain) {
        if (remain == "") {
            return true;
        }
        for (var word of wordDict) {
            if (remain.startsWith(word)) {
                var res = deepin(remain.slice(word.length, remain.length));
                if (res) {
                    return true;
                }
            }
        }
        return false
    };
    return deepin(s);
};
// @lc code=end

