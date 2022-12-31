#
# @lc app=leetcode.cn id=202 lang=python
#
# [202] 快乐数
#
# 解法1(无法AC): 按照题干描述不断重复这个步骤，如果==1则为True，关键在于什么时候该停下来，起初是算了一次2发现最终会变为20，于是设定条件为如果某次循环完整除原数是10的倍数，但有错例130，因为10//13会直接等于0；后来又试了几个数，将终止条件改为如果算完是10 100 1000这类则为True，否则如果等于原数或此时为10的倍数 比如20则为False，但错例536；后来又将终止条件改为字符串排序后是否与原数相等但超时    
#   改进1(T23% S66%): 终止条件为循环100次 emmmmm
#   改进2(T80% S85%): 终止条件为当前数>1 and <7 ，说是会停在这样一个循环里 `4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4`
# 
# 解法2(T80% S18%): 字典存储之前处理过的数字
# 
# 解法3(T93% S9%): 快慢指针，slow fast都初始化为n，两个指针分别自己跑自己的循环，如果有一个为1则True，如果二者相等则False
#   单独包装成一个函数要耗空间（但耗得很少，只是比例在那显得大）
#   改进(T93% S80%)：直接用slow fast复制多段循环代码，直接看逻辑可能有点乱，不推荐这么写太容易懵了

# @lc code=start
class Solution(object):
    def aLoop(self, n):
        buf = 0
        while n:
            buf += (n%10)**2
            n //= 10
        return buf
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n, n
        while True:
            slow = self.aLoop(slow)
            fast = self.aLoop(self.aLoop(fast))

            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False


    def loopSolution(self, n):
        # 解法3 改进
        buf = 0
        slow, fast = n, n
        while True:
            while slow:
                buf += (slow%10)**2
                slow //= 10
            slow = buf
            buf = 0

            while fast:
                buf += (fast%10)**2
                fast //= 10
            fast = buf
            buf = 0
            while fast:
                buf += (fast%10)**2
                fast //= 10
            fast = buf
            buf = 0

            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False

    def otherSolution(self, n):
        # 解法2
        buf = 0
        table = set()
        while True:
            while n:
                buf += (n%10)**2
                n //= 10
            if buf==1:
                return True
            
            if buf in table:
                return False
            table.add(buf)

            n = buf
            buf = 0

        # 解法1 改进2
        buf = 0
        while True:
            while n:
                buf += (n%10)**2
                n //= 10
            if buf==1:
                return True
            elif buf > 1 and buf < 7:
                return False
            n = buf
            buf = 0
# @lc code=end

