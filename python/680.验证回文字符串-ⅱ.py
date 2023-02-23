#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# 解法1(T65% S80%)：允许有一位不同，那就意味着正常双指针做回文的判断时可能会在中间卡一下二者不匹配，此时有两种可能，左指针删除当前字符后面还能是回文，右指针删除当前字符前面还能是回文，反正都只是一重循环不妨二者都尝试一下，没必要非要决定好到底是哪个字符多了，因为很可能测试样例耍赖造一个两侧极度相像的来欺骗

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(part):
            i, j = 0, len(part)-1
            while i<j:
                if part[i] != part[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

        flag = False
        i, j = 0, len(s)-1
        while i<j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        return valid(s[i+1:j+1]) or valid(s[i:j])
# @lc code=end

