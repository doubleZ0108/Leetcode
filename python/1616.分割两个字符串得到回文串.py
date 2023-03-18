#
# @lc app=leetcode.cn id=1616 lang=python3
#
# [1616] 分割两个字符串得到回文串
#
# 解法1(超时 75/110？)：按照题意正常的一重循环切片两字符串作，这样超时也很正常，切片、拼接，内层还要一重循环判断是否为回文串很费时间
#
# 解法2(T37% S38%)：其实本质上相当于left从一个字符串的头开始找，right从另一个字符串的尾开始找，如果二者交叉了，那把第一个的前半段和后半段拼起来就一定能构成回文串，但如果没交叉也还有一种可能：如果中间那段恰好本来就是回文串也可以的。同时需要注意因为a和b都可以做头，因此两种情况都要考虑

# @lc code=start
class Solution:
    # 解法2
    def check(self, s):
        i, j = 0, len(s)-1
        while i<j:
            if s[i]!=s[j]: return False
            i += 1
            j -= 1
        return True

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self._checkPalindromeFormation(a, b) or self._checkPalindromeFormation(b, a)

    def _checkPalindromeFormation(self, a, b):
        left, right = 0, len(a)-1
        while left < len(a) and a[left]==b[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        return self.check(a[left:right+1]) or self.check(b[left:right+1])


    # 解法1 超时
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(s):
            i, j = 0, len(s)-1
            while i<j:
                if s[i]!=s[j]: return False
                i += 1
                j -= 1
            return True

        for i in range(0, len(a)+1):
            a_pre, a_suf = a[0:i], a[i:]
            b_pre, b_suf = b[0:i], b[i:]
            s1, s2 = a_pre + b_suf, b_pre + a_suf
            if check(s1) or check(s2):
                return True
        return False
# @lc code=end

