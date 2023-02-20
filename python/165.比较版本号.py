#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#
# 解法1(T40% S5%)：首先将两个字符串版本号根据.划分，并将每位修订号转换为整数，这样自动就去除了前导0带来的影响，然后按照最大数组长度同步循环两拆分好后的修订好，如果下标超了就意味着这个版本号在这位默认0，最后只需要比较哪个修订号更大即可

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vers1 = list(map(lambda x: int(x), version1.split(".")))
        vers2 = list(map(lambda x: int(x), version2.split(".")))
        for i in range(max(len(vers1), len(vers2))):
            v1 = vers1[i] if i<len(vers1) else 0
            v2 = vers2[i] if i<len(vers2) else 0
            if v1 > v2: 
                return 1
            elif v1 < v2: 
                return -1
        return 0
# @lc code=end

