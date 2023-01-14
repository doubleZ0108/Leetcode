/*
 * @lc app=leetcode.cn id=468 lang=javascript
 *
 * [468] 验证IP地址
 */

// @lc code=start
/**
 * @param {string} queryIP
 * @return {string}
 */
var validIPAddress = function(queryIP) {
    var isIPv4 = function(ip) {
        var tokens = ip.split(".");
        if (tokens.length != 4) { return false; }
        for (var token of tokens) {
            if (token == "" || (token.length>1 && token[0]=='0')) { return false; }
            for (var ch of token) {
                if (!(ch>='0' && ch<='9')) { return false; }
            }
            var itoken = parseInt(token);
            if (itoken>255) { return false; }
        }
        return true;

    };
    var isIPv6 = function(ip) {
        var tokens = ip.split(":");
        if (tokens.length != 8) { return false; }
        for (var token of tokens) {
            if (token.length==0 || token.length>4) { return false; }
            for (var ch of token) {
                if (!((ch>='0' && ch<='9') || (ch>='a' && ch<='f') || (ch>='A' && ch<='F'))) { return false; }
            }
        }
        return true;
    };

    if (isIPv4(queryIP)) {
        return "IPv4";
    } else if (isIPv6(queryIP)) {
        return "IPv6";
    } else {
        return "Neither";
    }
};
// @lc code=end

