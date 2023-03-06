#
# @lc app=leetcode.cn id=1108 lang=python3
#
# [1108] IP 地址无效化
#
# 解法1(T85% S99%)：没太明白这道题想干嘛，直接调用Python的replace()函数即可

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
# @lc code=end

