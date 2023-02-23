#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
# 解法1(T99% S92%)：由于题干的逆波兰表达式非常干净，也没有括号啥的，遇到运算符时一定满足前面有两个操作数，通过一个栈维护，如果是数字则直接压栈，如果是操作符就弹出两个操作数运算，注意最后一个元素是右操作数，倒数第二个元素是左操作数，二者的顺序不能搞反了
#     本题唯一新的知识点是，Python的向零取整就直接是`int()`

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        S = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in S:
                stack.append(int(token))
            else:
                r, l = stack.pop(), stack.pop()
                calc = None
                if token == '+':
                    calc = l + r
                elif token == '-':
                    calc = l - r
                elif token == '*':
                    calc = l * r
                else:
                    calc = int(l / r)
                stack.append(calc)
        return stack[-1]

# @lc code=end

