#
# @lc app=leetcode.cn id=2299 lang=python3
#
# [2299] 强密码检验器 II
#
# 解法1(T5% S7%)：直接用python的filter语法过滤条件，如果过滤后元素个数位0则返回false
#
# 解法2(T50% S47%)：一重循环来解决，设定四个flag判断是否出现过大小写数字和特殊字符，初始都设为True，第一次满足条件时将其变为False，最后的返回结果就是如果有一个人还是True，则代表那种情况没被满足就应该返回False，所以通过not ( or )结构来逻辑判断即可。还有一个小点是将特殊字符转换为集合查找会快一点

# @lc code=start
class Solution:
    # 解法2
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        lowflag, upflag, numflag, speflag = True, True, True, True
        specials = set([_ for _ in "!@#$%^&*()-+"])

        for i in range(len(password)):
            if lowflag and (ord(password[i])>=ord('a') and ord(password[i])<=ord('z')):
                lowflag = False
            if upflag and (ord(password[i])>=ord('A') and ord(password[i])<=ord('Z')):
                upflag = False
            if numflag and (ord(password[i])>=ord('0') and ord(password[i])<=ord('9')):
                numflag = False
            if speflag and password[i] in specials:
                speflag = False
            if (i>0 and password[i-1]==password[i]):
                return False
        return not (lowflag or upflag or numflag or speflag)

    # 解法1
    def strongPasswordCheckerII1(self, password: str) -> bool:
        if len(password) < 8 or \
            len(list(filter(lambda x: ord(x)>=ord('a') and ord(x)<=ord('z'), password))) == 0 or \
            len(list(filter(lambda x: ord(x)>=ord('A') and ord(x)<=ord('Z'), password))) == 0 or \
            len(list(filter(lambda x: ord(x)>=ord('0') and ord(x)<=ord('9'), password))) == 0 or \
            len(list(filter(lambda x: x in "!@#$%^&*()-+", password))) == 0:
            return False

        for i in range(1, len(password)):
            if (password[i-1]==password[i]):
                return False
        return True
# @lc code=end

