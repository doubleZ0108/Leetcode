#
# @lc app=leetcode.cn id=2283 lang=python3
#
# [2283] 判断一个数的数字计数是否等于数位的值
#
# 解法1(T74% S68%)：首先一次遍历统计每个位的数位值出现多少次（可以通过哈希表或bitmaps因为只有数字），再一次遍历判断每一位的数值是否等于哈希表中储存的数字出现计数即可

# @lc code=start
class Solution:
    def digitCount(self, num: str) -> bool:
        table = Counter([s for s in num])
        for i in range(len(num)):
            if int(num[i]) != table[str(i)]:
                return False
        return True
# @lc code=end

