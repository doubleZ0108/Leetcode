/*
 * @lc app=leetcode.cn id=929 lang=javascript
 *
 * [929] 独特的电子邮件地址
 */

// @lc code=start
/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    var set = new Set();
    for (var email of emails) {
        var parts = email.split("@");
        var local = parts[0], site = "@".concat(parts[parts.length-1]);
        var valid = local.split("+")[0].split(".").join("");
        set.add(valid.concat(site));
    }
    return set.size;
};
// @lc code=end

