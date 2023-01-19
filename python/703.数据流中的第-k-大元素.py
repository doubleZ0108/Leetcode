#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#
# 解法1(T29% S5%)：通过集成好的优先队列/堆来实现，`init`时初始化堆，`add`时首先堆插入，再提取第k大元素
#     - `SortedList`可以完成但性能有限
#     - `heapq`直接调用nlargest()再取最后一个元素会超时（9/10）
#
# 改进1(T86% S75%)：堆中只维护k个数，数据流的题要注意数据可能源源不断的加入，如果把所有数都存下来不仅占空间二者还增加查找的复杂度，因为本地还要返回第k大的数，所以很小的那些数就可以直接扔掉了，因为之后肯定用不上他们
#     - `init`：初始化堆，并不断弹出最小值直到堆中元素个数不超过k个
#     - `add`：先直接将元素压堆，如果长度超过k了，则先弹出一个元素，这样堆中始终有且只有k个元素，那么堆顶就是第k大的元素

# @lc code=start
from sortedcontainers import SortedList

# 改进1
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.H = nums
        heapq.heapify(self.H)
        while (len(self.H) > self.k):
            heapq.heappop(self.H)

    def add(self, val: int) -> int:
        heapq.heappush(self.H, val)
        if len(self.H) > self.k:
            heapq.heappop(self.H)
        return self.H[0]

# 解法1
class KthLargest1:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.sl = SortedList(nums)

    def add(self, val: int) -> int:
        self.sl.add(val)
        return self.sl[len(self.sl)-self.k]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

