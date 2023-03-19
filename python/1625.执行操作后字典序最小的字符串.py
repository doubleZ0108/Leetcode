#
# @lc app=leetcode.cn id=1625 lang=python3
#
# [1625] 执行操作后字典序最小的字符串
#
# 解法1(T8% S81%)：看到这种不知道可能循环多少次的，肯定是类似BFS DFS这类的思想，通过visited来去重，这样就可以达到有限次循环了。就本题而言，因为只有两种变换方式，那我们不妨就对每个变换后的结果都分别施加这两个变换，因为只是找最优结果又没问最少多少步，所以代码写起来也问题不大

# @lc code=start
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        res = s
        visited = set([s])
        queue = [s]
        while queue:
            this = queue.pop(0)
            if this < res:
                res = this

            this1 = [int(ch) for ch in this]
            for i in range(len(this1)):
                if i % 2 == 1:
                    this1[i] = (this1[i] + a) % 10
            this1 = "".join([str(ch) for ch in this1])
            if this1 not in visited:
                queue.append(this1)
                visited.add(this1)

            this2 = this[-b:] + this[:-b]
            if this2 not in visited:
                queue.append(this2)
                visited.add(this2)
        return res
# @lc code=end

