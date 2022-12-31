#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#
# 解法1(T89% S98%): 双栈倒腾一次就可以实现队列
#   push的时候左栈放进去
#   pop的时候如果右栈有东西就直接pop，否则先把左栈的东西倒腾到右栈，右栈弹出最上面的
#   peak和pop可以不分代码复用

# @lc code=start
class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)


    def pop(self):
        """
        :rtype: int
        """
        ans = self.peek()
        self.stack2.pop()
        return ans


    def peek(self):
        """
        :rtype: int
        """
        if self.stack2:
            return self.stack2[-1]
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

