#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#
# 解法1(T55% S78%)：题目思路很好想，肯定是双指针处理，但很多小条件还是需要通过错误提交几次看看边界小例子的。核心思路为，如果name中有连续相同的字符，那前面的只能一位一位跟typed比较，但如果是最后一个连续字符或者是一个独立的字符，则允许用户长按多次，此时通过一个while循环将typed的指针往后移动。有几种False的情况：1）当前i和j指向的字符不同，这也是最好想的；2）j此时已经越界了，代表typed比name少了后半截；3）i看完了但j后面还多了一截，且这一截跟i末尾的字符不一样。这题的困难点在于一下子想清楚所有可能的情况，还是通过几个错误的例子来找边界条件比较好

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name): return False
        elif len(typed) == len(name) and typed != name: return False

        i, j = 0, 0
        while i<len(name):
            if i+1<len(name) and name[i+1]==name[i]:
                if name[i] == typed[j]:
                    i += 1
                    j += 1
                else:
                    return False
            else:
                if j>=len(typed):
                    return False
                if name[i] != typed[j]:
                    return False
                while j<len(typed) and typed[j] == name[i]:
                    j += 1
                i += 1
        if j<len(typed) and typed[j]!=name[-1]:
            return False
        return True

# @lc code=end

