#
# @lc app=leetcode.cn id=929 lang=python
#
# [929] 独特的电子邮件地址
#
# 解法1(T85% S90%)：不要把题想复杂了，就是让你判断是否重复，没让你判断是否valid（默认本地名和域名都是合法的），直接通过一个函数封装一个邮件地址的目的地，主要是考python的字符串处理库函数，首先通过split()划分@左右为本地名和域名，然后对于本地名如果+在其中，则通过切片和index()截断后面的不要，最后去掉.可以通过先split()后join()的方式处理，最终返回(目的地, 域名)元组并通过set去重复

# @lc code=start
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def toWhom(email):
            li = email.split('@')
            local, domain = li[0], li[-1]
            if '+' in local:
                local = local[:local.index('+')]
            local = "".join(local.split('.'))
            return(local, domain)


        s = set()
        for email in emails:
            s.add(toWhom(email))
        
        return len(s)

Solution().numUniqueEmails(["test.email+alex@leetcode.com", "test.email@leetcode.com"])
# @lc code=end

