/*
 * @lc app=leetcode.cn id=5 lang=java
 *
 * [5] 最长回文子串
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        String res = Character.toString(s.charAt(0));
        for (int i=0; i<s.length(); ++i) {
            int left=i, right=i;
            while (right+1<s.length() && s.charAt(right+1) == s.charAt(i)) { 
                ++right; 
            }
            while (left-1>-1 && right+1<s.length() && s.charAt(left-1)==s.charAt(right+1)) {
                --left;
                ++right;
            }
            if (right-left+1 > res.length()) {
                res = s.substring(left, right+1);
            }
        }
        return res;
    }
}
// @lc code=end

