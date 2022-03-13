#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#
# 解法1(T99% S95%): 标准栈求解，左括号一路压栈，右括号弹出匹配，当前指向`)`，必须满足栈顶弹出来的是`(`
#   小trick：可以用字典把括号的对应存下来，可以避免很多相似结构代码；同时pop()本身放在if- else里也是很漂亮的代码
#   提前判断是否为奇数

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False

        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for item in s:
            if item not in bracket_map:
                stack.append(item)
            elif len(stack)==0 or stack.pop() != bracket_map[item]:
                return False
        return not stack
# @lc code=end

