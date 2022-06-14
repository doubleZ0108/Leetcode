#
# @lc app=leetcode.cn id=933 lang=python
#
# [933] 最近的请求次数
#
# 解法1(T31% S62%)：维护一个队列，每次ping()时，都首先让所有超出时间范围内的之前请求pop()出队，然后队尾添加新请求并返回当前队列的总长度即可（这样可以最高效经济的处理）

# @lc code=start
class RecentCounter:

    def __init__(self):
        self.lasts = []


    def ping(self, t: int) -> int:
        while self.lasts:
            if self.lasts[0] < t-3000: self.lasts.pop(0)
            else: break
        self.lasts.append(t)
        return len(self.lasts)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

