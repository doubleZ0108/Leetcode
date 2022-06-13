#
# @lc app=leetcode.cn id=933 lang=python
#
# [933] 最近的请求次数
#

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

