#
# @lc app=leetcode.cn id=1797 lang=python3
#
# [1797] 设计一个验证系统
#
# 解法1(T55% S98%)：没有很复杂，通过一个哈希表来维护即可
#     `generate()`：因为题中条件说token不会重复，因此直接加入哈希表即可
#     `renew()`：首先判断token是否合法（存在且没过期），更新时间
#     `count()`：对于哈希表中每个元素判断是否过期，如果过期则删除否则计数，一般这种一边遍历一遍删除的可能会出问题，所以推荐把所有过期的key先保存在数组里，再单独一次遍历删除会比较稳妥

# @lc code=start
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.table = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.table[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.table:
            return
        if self.table[tokenId]+self.timeToLive <= currentTime:
            return
        self.table[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        tmp = []
        for key, val in self.table.items():
            if val+self.timeToLive <= currentTime:
                tmp.append(key)
            else:
                res += 1
        for key in tmp:
            self.table.pop(key)
        return res



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
# @lc code=end

