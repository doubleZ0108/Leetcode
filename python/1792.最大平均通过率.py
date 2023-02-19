#
# @lc app=leetcode.cn id=1792 lang=python3
#
# [1792] 最大平均通过率
#
# 解法1：暴力法直观一想，有很多班级很多聪明学生，那只能不断模拟，把一定数目的聪明学生依次加入每个班级找最大值，仔细一想肯定会超时，因为究竟把多少学生放到哪些班级，这样的排列组合方式太多了，肯定不行
#
# 解法2(T8% S5%)：我们先来考虑一个极端情况，如果某个班级之前的通过率就是100%，那就没必要给这个班级增加聪明学生，因为加完之后还是100%没有任何提升，因此顺理成章的我们考虑另外一头的极端情况，如果一个本来很差的班级，给他加上一个聪明学生，这个班级的通过率会有很大的提升，进而所有班级的平均通过率也会很大提升，因此我们发现每次找当前最差的那个班级就好。那现在问题变成了，我一个一个聪明学生的给，每轮最差的班级是哪个呢？我们设A为某班级当前的passi，N为班级的totali，加一个聪明学生的通过率变化为$\frac{A}{N} \rightarrow \frac{A+1}{N+1}$，我们计算二者的变化值$\Delta = \frac{N-A}{(N+1)N}$，我们希望每次找这个变化率最大的那个班级，给他加一个聪明学生。现在问题就很直观了，我们只需要通过一个优先队列（堆）来维护这个$\Delta$，每次找最大的那个班级，给他添加一个聪明学生，并更新班级的通过率
#     本题代码写的比较啰嗦导致时间空间占用比较大，但道理上是没问题的

# @lc code=start
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        for i in range(len(classes)):
            A, N = classes[i][0], classes[i][1]
            classes[i].append(A/N)
            classes[i].append((N-A)/(N*N+N))

        from sortedcontainers import SortedList
        sl = SortedList(classes, key=lambda x: x[-1])
        for i in range(extraStudents):
            lowest = sl.pop()
            A, N = lowest[0]+1, lowest[1]+1
            sl.add([A, N, A/N, (N-A)/(N*N+N)])

        return sum([x[2] for x in sl]) / len(classes)
# @lc code=end

