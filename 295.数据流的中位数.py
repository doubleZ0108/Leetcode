#
# @lc app=leetcode.cn id=295 lang=python
#
# [295] 数据流的中位数
#
"""
解法1(超时)：维护一个数组长度和一个数组，每次添加新数字时首先把数字放到数组尾部，然后进行一次插入排序的动作让数组保持有序；获取中位数时直接按照奇偶选择最中间的元素就好
    改进1(超时)：将普通数组换成优先队列，每次插入时可以直接让优先队列有序，每次获取中位数时可以直接通过`nlargest`获取中间位置附近的两个数
    
解法2(T93% S23%)：维护两个优先队列，minheap元素都比中位数小，maxheap元素都比中位数大，这样每次获取中位数时只需看两个队列长度是否相等，如果想等就代表肯定是偶数个，则返回两队列对头元素的平均值，如果不相等直接返回长的队列的队头即可。那具体怎么维护这两个优先队列呢？可以先考虑minheap，如果之前为空或者当前要进来的元素比minheap最大的元素还小，则证明新插入的这个数肯定也比中位数小，那它应该放在minheap里，反之应该放在maxheap里，同时为了保证两队列的平均性，每次插入之后如果某个队列比另一个长度大1以上，则应该把一个元素拿出来放到另一个队列中
"""

import heapq

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap or num <= -self.minheap[0]:
            heapq.heappush(self.minheap, -num)
            if len(self.minheap) > len(self.maxheap)+1:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        else:
            heapq.heappush(self.maxheap, num) 
            if len(self.maxheap) > len(self.minheap)+1:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (-self.minheap[0] + self.maxheap[0]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return -self.minheap[0]
        else:
            return self.maxheap[0]

"""
# 解法1 超时
class MedianFinder:

    def __init__(self):
        self.N = 0
        self.arr = []


    def addNum(self, num: int) -> None:
        self.N += 1
        self.arr.append(num)
        i = self.N-2
        while i>-1 and num<self.arr[i]:
            self.arr[i+1] = self.arr[i]
            i -= 1
        if i!=self.N-2: 
            self.arr[i+1] = num


    def findMedian(self) -> float:
        if self.N % 2 == 0:
            return (self.arr[self.N//2-1] + self.arr[self.N//2]) / 2
        else:
            return self.arr[self.N//2]
"""


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

