#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
# 解法1(T41% S30%)：虽然实现的感觉有点暴力，但能用，本身这个问题就不太科学，还是反向的问题用栈实现队列比较有趣
#     `init`：初始化两个空队列
#     `push`：直接加入左队列尾部
#     `pop`：不断把左队列的元素出队放到右队列里，直到左队列只剩一个元素，然后交换两个队列，这样右队列中存在的唯一元素就是返回的结果
#     `top`：跟pop类似，区别在于取完值之后要把右队列的元素再放回左队列里，要么就乱套了

# @lc code=start
class MyStack:

    def __init__(self):
        self.left, self.right = [], []


    def push(self, x: int) -> None:
        self.left.append(x)

    def pop(self) -> int:
        while len(self.left)>1:
            self.right.append(self.left.pop(0))
        self.left, self.right = self.right, self.left
        return self.right.pop(0)

    def top(self) -> int:
        while len(self.left)>1:
            self.right.append(self.left.pop(0))
        self.left, self.right = self.right, self.left
        tmp = self.right[0]
        self.left.append(self.right.pop(0))
        return tmp


    def empty(self) -> bool:
        return self.left==[] and self.right==[]



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

