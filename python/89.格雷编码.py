#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = ["0"*n]
        for i in range(1, 2**n, 2):
            last = res[-1]
            res.append(last[:-1] + str(1 - int(last[-1])))

            last = res[-1]
            j = n-1
            while j>-1 and last[j]!='1':
                j -= 1
            if j != 0:
                j -= 1
            res.append(last[:j] + str(1 - int(last[j])) + last[j+1:])
        res.pop()
        return [int(x, 2) for x in res]
# @lc code=end

