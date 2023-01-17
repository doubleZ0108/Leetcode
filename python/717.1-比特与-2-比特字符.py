#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1 比特与 2 比特字符
#
# 解法1(T78% S78%)：题目有点点怪，首先处理特殊情况，如果只有1位那只能是0，如果倒数第二位是0，则一定只能用1比特来做；否则从头开始循环，如果某位是1，那只能通过2比特来做，则下标一次加2，否则下标一次加1，到倒数第二位之前终止，如果剩下的是[0]，那只能通过1比特实现，否则一定剩下的是[1,0]则不需要

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1: return True
        if bits[-2] == 0: return True
        i = 0
        while i<len(bits)-2:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        
        return bits[i:]==[0]
        
# @lc code=end

