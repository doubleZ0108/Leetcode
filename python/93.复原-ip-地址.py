#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#
# 解法1(T10% S98%)：题目还是很有趣的，本质相当于在原字符串中加三个.使得分割得到的ip地址有效，因为只有三个分割，那不妨通过三重循环来做，对于每一个可能的下标分割方式，判断每个字段是否成立：只有一位或前导位不是0，并且数组介于月0～255

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        for i in range(1, len(s)-2):
            for j in range(i+1, len(s)-1):
                for k in range(j+1, len(s)):
                    fields = [s[:i], s[i:j], s[j:k], s[k:]]
                    if all([(len(field)==1 or field[0]!='0') and (int(field)>=0 and int(field)<=255) for field in fields]):
                        res.append(".".join(fields))
        return res
# @lc code=end

