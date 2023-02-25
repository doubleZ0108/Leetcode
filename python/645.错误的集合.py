#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#
# 解法1(T47% S5%)：首先先用Counter()统计每个数字出现的个数，然后对item按照value排序，排序完的第一个元素就是重复了一遍的元素；缺失的元素直接通过集合的交集得到就可以
#     稍微有点浪费了，就只有一个元素重复废了这么大阵仗，但whatever

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        num1 = sorted(cnt.items(), key=lambda x: x[1])[-1][0]
        num2 = list(set(range(1, len(nums)+1)) - cnt.keys())[0]
        return [num1, num2]

# @lc code=end

