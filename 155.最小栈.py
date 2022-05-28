#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#
# 解法1(T92% S90%)：数据结构设计题。在栈的基础上能在常数时间获取到最小值，因此肯定需要把最小值存下来，在push和pop时维护，这里使用一个类内变量存储
#   `push()`：加到栈顶，如果比当前最小值小则更新
#   `pop()`：弹出栈顶，如果此时弹出的就是最小值则一次遍历更新最小值，如果栈为空则将最小值归为None
#   `top()`：直接返回栈顶（题目保证在栈非空时调用）
#   `getMin()`：直接返回最小值（题目保证在栈非空时调用）

# @lc code=start
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minVal = None


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minVal is None or val < self.minVal:
            self.minVal = val


    def pop(self) -> None:
        re = self.stack.pop(-1)
        if re == self.minVal:
            if self.stack != []:
                self.minVal = self.stack[-1]
                for val in self.stack:
                    if val < self.minVal: self.minVal = val
            else: self.minVal = None
        


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

