#
# @lc app=leetcode.cn id=468 lang=python
#
# [468] 验证IP地址
#
# 解法1(T99% S69%)：按照题干要求写if就可以了。首先通过split()将字符串进行划分，然后根据IPv4和IPv6的规则写if把不满足条件的剔除即可。要注意的IPv4不能有前导0，但可以某一位就是0。提示：可以通过isnumeric()判断字符串是否为数字。

# @lc code=start
class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        def isIPv4(ip):
            parts = ip.split('.')
            if len(parts) != 4: return False
            for part in parts:
                if len(part)==0 or not part[0].isnumeric() or not part.isnumeric() or \
                   int(part) > 255: return False
                if len(part)>1 and part[0]=='0': return False
            return True

        def isIPv6(ip):
            parts = ip.split(':')
            if len(parts) != 8: return False
            for part in parts:
                if len(part) < 1 or len(part) > 4: return False
                for c in part:
                    if c.isnumeric() or (c>='a' and c<='f') or (c>='A' and c <='F'): continue
                    return False
            return True

        if isIPv4(queryIP): return "IPv4"
        elif isIPv6(queryIP): return "IPv6"
        else: return "Neither"
# @lc code=end

