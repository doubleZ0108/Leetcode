#
# @lc app=leetcode.cn id=1815 lang=python3
#
# [1815] 得到新鲜甜甜圈的最多组数
#
# 解法1(超时 3/74)：本来是看到数组长度最多为30，想用全排列试一试，但还是太天真，$2^{30}$还是太大了。首先将原数组每个数对batchsize取余，减小数字规模，然后构建全排列，对每种可能的排列结果循环，用一个变量remain刻画当前剩余，如果remain==0则代表该顾客开心，remain再减去顾客的购买数，如果remain<0则需要再烤batchsize个
#     改进0：提前终止，如果某次排列所有顾客都开心则直接返回；如果当前排列中循环的剩余人数都没有当前最多开心人数多则也可以跳过
#     改进1(超时10/74)：先统计购买数是batchsize整数倍的人们，可以提前安排他们，他们一定会开心，降低问题规模
#
# 解法2：解法1中自己对问题的理解还是可以的，初始化的操作也都正确，但用全排列的方法肯定不行，标准答案使用了位运算、状态压缩、状态转移来做，简单来说就是取余之后每个人的购买数最多只有8种可能，不妨令$a_0 a_1...a_7$代表一个购买情况，意思就是买i个甜甜圈的人有$a_i$，现在就是要求这样最好的一种排列
#
# 解法3(T24% S98%)：模拟退火。计算某个排列的结果还是如解法1所示的，非常简洁，同样的，在排除了特殊情况后进入模拟退火。首先随机打乱数组，然后设定温度从高到低迭代，每次随机选择两个下标，先计算交换前的值，再计算交换后的值，如果交换完可以带来增益（交换完计算结果更大），则保留这个交换，否则就不交换了（正常应该设定一定的概率不交换，但发现没法AC73例）。
#     - 其中模拟总次数27，温度设定5e4 → 1e-5，0.97的退货率都是参考其他人的题解设置的，这种优化方式还是非常神奇的

# @lc code=start
class Solution:
    def __init__(self):
        self.res = 0

    # 解法3 模拟退火
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize==1: return len(groups)

        newgroups = []
        res0 = 0
        for group in groups:
            if group % batchSize==0: res0 += 1
            else: newgroups.append(group % batchSize)

        if len(newgroups) <=1:
            return res0 + len(newgroups)

        def cal():
            remain, thisres = 0, 0
            for buy in newgroups:
                if remain == 0:
                    thisres += 1
                remain -= buy
                if remain < 0:
                    remain += batchSize
            self.res = max(self.res, thisres)
            return thisres

        def simulate_annel():
            random.shuffle(newgroups)
            t = 5e4
            while t>1e-5:
                i, j = random.randint(0, len(newgroups)-1), random.randint(0, len(newgroups)-1)
                x = cal()
                newgroups[i], newgroups[j] = newgroups[j], newgroups[i]
                y = cal()

                delta = y - x
                if delta<0: # and math.exp(delta/t)<random.random():
                    newgroups[i], newgroups[j] = newgroups[j], newgroups[i]

                t *= 0.97
        
        for i in range(27):
            simulate_annel()
        return res0 + self.res


    # 解法1 超时
    def maxHappyGroups1(self, batchSize: int, groups: List[int]) -> int:
        groups = [x%batchSize for x in groups]
        res0 = groups.count(0)
        newgroup = list(filter(lambda x: x!=0, groups))

        maxres = 0
        for perm in itertools.permutations(newgroup, len(newgroup)):
            remain, res = 0, 0
            for i, buy in enumerate(perm):
                if len(newgroup)-i-1+res < maxres: break
                if remain == 0:
                    res += 1
                remain -= buy
                if remain < 0:
                    remain += batchSize

            maxres = max(maxres, res)
            if maxres == len(newgroup): break
        return maxres+res0
# @lc code=end

