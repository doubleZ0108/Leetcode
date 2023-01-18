#
# @lc app=leetcode.cn id=1825 lang=python3
#
# [1825] 求出 MK 平均值
#
# 解法1(超时 13/17)：队列 + 一个临时堆。按照题目描述，通过一个队列来维护最新的m个数，求取mka的时候将其转为一个堆获取最小的k个数和最大的k个数。但缺点也很明显，每次计算时都要堆标准化一次，还要计算求和等等，大数肯定会超时。
#     `add`：先把num加入队列，如果队列长度超过m，则删除最左侧的一个元素，维持队列长度始终不超过m
#     `cal`：如果队列长度还不够m则直接返回-1，否则将队列转为数组再转为堆，通过堆可以较高效的获取k个最大值和k个最小值，然后通过sum()求和就可以计算出mka
# 
# 解法2(T11% S90%)：队列 + 三个堆。解法1的问题也很明显，每次都要重复计算求和，肯定通过维护一个变量直接保存满足元素的和会更好；另一方面，每次都要重新获取k个最小和k个最大，很明显很多数都是不变的，因此也应该通过某种数据结构维护k个最小的数和k个最大的数。但比较麻烦的因为这是数据流，最先加入的数一定时间后会过期，所以队列还是必不可少维护最后m个数的方式。
#     `init`：除了队列dq外；通过三个优先队列（堆）来维护k个最小的数smal，k个最大的数large和中间mid用来求解mka的数组；再引入一个变量midsum用来记录中间数字的大小
#     `add`：首先无脑将num加入small，因为如果small中没有k个数那之后肯定也不好求mka（因为mka的计算要排除k个最小的数），如果small中数字个数超过k个了，则把最大的数弹出加入large，同理，如果large中没有k个数也不行；接着，如果large中数也超过了k个，则从中弹出最小值加入mid，此时记得维护下midsum。考虑完进，现在要考虑太老的数据出的问题了，还是通过dq来维护，如果当前数字总数超过m了，则要在dp中弹出最先进队的元素，那相应的也要在small mid large中删除该元素，删除没什么新颖的，就直接.remove()即可，但需要注意，small和large要始终有k个元素，所以如果被删除的元素在small中，则要把mid中最小的数移入small中，还要维护下midsum，同理large
#     `cal`：计算就很简单了，因为我们维护了midsum，直接用它除以数字总个数就可以了

# > 关于维护优先队列这里采用了SortedList，因为heapq默认只能小根堆，因此small就要通过负数来维护，代码里面时不时要注意正负号转换有点麻烦，SortedList默认也是从小到大排序，0元素就是最小元素，-1元素就是最大元素，比较方便，不需要一定通过heappush和heappop来操作
# >

# @lc code=start
from sortedcontainers import SortedList

# 解法2
class MKAverage:

    def __init__(self, m: int, k: int):
        self.dq = deque()
        self.m = m
        self.k = k
        self.small, self.mid, self.large = SortedList(), SortedList(), SortedList()
        self.midsum = 0

    def addElement(self, num: int) -> None:
        self.small.add(num)
        if len(self.small) > self.k:
            self.large.add(self.small.pop())
            if len(self.large) > self.k:
                tmp = self.large.pop(0)
                self.mid.add(tmp)
                self.midsum += tmp
        self.dq.append(num)
        if len(self.dq) > self.m:
            tmp = self.dq.popleft()
            if tmp in self.small:
                self.small.remove(tmp)
                self.midsum -= self.mid[0]
                self.small.add(self.mid.pop(0))
            elif tmp in self.large:
                self.large.remove(tmp)
                self.midsum -= self.mid[-1]
                self.large.add(self.mid.pop())
            else:
                self.midsum -= tmp
                self.mid.remove(tmp)

    def calculateMKAverage(self) -> int:
        if len(self.dq) < self.m:
            return -1
        else:
            return self.midsum // (self.m - 2*self.k)


# 解法1 超时
class MKAverage1:

    def __init__(self, m: int, k: int):
        self.data = deque()
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        self.data.append(num)
        if len(self.data) > self.m:
            self.data.popleft()

    def calculateMKAverage(self) -> int:
        if len(self.data) < self.m:
            return -1

        heapq.heapify(list(self.data))
        nl = heapq.nlargest(self.k, self.data)
        ns = heapq.nsmallest(self.k, self.data)
        avg = (sum(self.data) - sum(nl) - sum(ns)) / (self.m-2*self.k)
        return floor(avg)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
# @lc code=end

