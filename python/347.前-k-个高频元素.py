#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#
# 解法1(T97% S91%): 乍一看很像堆的题，但最终要找的是次数最大的几个，因此不用那么复杂。首先一次循环用字典储存每个元素出现的次数，然后按照value对dict排序，排序后得到的是一个二元数组，选取前k个数组元素输出key就好
# 
# 解法2(T71% S81%): 确实也可以通过堆来做，首先还是一次遍历获取统计字典，然后直接调用heapq的nlargest获取前k大个元素，key是table中的value
# 
# 解法3(T97% S43%): 还是用堆，不过堆插入删除的逻辑自己写。首先把所有table中的元素按照value值插入heap（python的heapq只能使用默认的最小堆），然后再循环进行根的pop直到剩下k个元素
#   改进1(T99% S80%): 全插入再删除太费时，堆中只要时刻维护k个数就可以了，对于统计完的table，首先执行k次push操作（这时候不用考虑其他），k次之后要判断最小堆顶的元素和准备进来的谁更大，只保留更大的就可以了，heapq中直接通过`heappushpop()`方法就可以一次实现插入当前元素并弹出最小元素

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 解法2
        table = {}
        for num in nums:
            if num in table: table[num] += 1
            else: table[num] = 1

        import heapq
        res = heapq.nlargest(k, table, key=lambda kk: table[kk])
        return res

    def otherSolution(self, nums, k):
        # 解法1
        table = {}
        for num in nums:
            if num in table: table[num] += 1
            else: table[num] = 1

        sorted_li = sorted(table.items(), key=lambda item: item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_li[i][0])

        return res

        # 解法3
        table = {}
        for num in nums:
            if num in table: table[num] += 1
            else: table[num] = 1

        import heapq
        res = []
        for key, value in table.items():
            heapq.heappush(res, [value, key])
        for i in range(len(res)-k):
            heapq.heappop(res)

        return [item[1] for item in res]

        # 解法3 改进1
        table = {}
        for num in nums:
            if num in table: table[num] += 1
            else: table[num] = 1

        import heapq
        res = []
        for key, value in table.items():
            if len(res) < k:
                heapq.heappush(res, [value, key])
            else:
                heapq.heappushpop(res, [value, key])


        return [item[1] for item in res]
# @lc code=end

