#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#
# 解法1(T40% S96%)：双指针判断各自指向的是否为相同的字符（如果是数字则相等，如果是字母则不考虑大小写，可以统一使用.lower()判断），因为除了数字和字母都要跳过，所以在while内部还要加两个while来过滤left和right值，可以使用.isalnum()判断是否为字母或数字

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum(): left += 1
            while left < right and not s[right].isalnum(): right -= 1
            if s[left].lower() != s[right].lower(): return False
            left += 1
            right -= 1
        return True
# @lc code=end

