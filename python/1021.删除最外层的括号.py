#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#
# 解法1(T94% S16%)：题干描述是真的啰嗦，直接看例子就能明白题目的意思，涉及括号配对的题肯定是通过栈来实现，当栈里只有一个(，且遇到)时就意味着这中间看到的部分是一个原语，因此核心逻辑就是当栈里一个(垫底的时候把遇见的所有内容都加到结果里，当遇到一个)让栈为空了则切换到另一个原语继续处理

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = [s[0]]
        res = ""
        for i in range(1, len(s)):
            if len(stack)==0:
                stack.append('(')
            elif s[i] == ')':
                stack.pop()
                if len(stack) != 0:
                    res += s[i]
            else:
                stack.append('(')
                res += s[i]
        return res
# @lc code=end

