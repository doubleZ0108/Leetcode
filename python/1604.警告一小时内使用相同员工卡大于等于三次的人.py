#
# @lc app=leetcode.cn id=1604 lang=python3
#
# [1604] 警告一小时内使用相同员工卡大于等于三次的人
#
# 解法1(T6% S6%)：解法偏暴力，因为人名数组和时间数组是对应的，所以要一起循环，因为不知道会有多少不同的人，所以通过哈希表来维护每个人的时间数组，因为将来要看一小时之内的时间肯定需要排序，那不如直接每个人的时间数组直接通过优先队列来维护，同时在存储的时候将时间字符串直接转换为分钟计数。整理完哈希表之后直接一次循环，看每个人的有序时间数组里是否存在分钟数60之内的情况，将结果统计到另一个优先队列维护的结果数组中即可

# @lc code=start
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from sortedcontainers import SortedList
        table = {}
        for name, time in zip(keyName, keyTime):
            second = int(time.split(":")[0]) * 60 + int(time.split(":")[-1])
            if name not in table:
                table[name] = SortedList([second])
            else:
                table[name].add(second)
        
        res = SortedList()
        for key, val in table.items():
            if len(val) >= 3:
                for i in range(2, len(val)):
                    if val[i] <= val[i-2]+60:
                        res.add(key)
                        break
        return list(res)
# @lc code=end

