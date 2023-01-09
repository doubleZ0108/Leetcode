#
# @lc app=leetcode.cn id=1806 lang=python3
#
# [1806] 还原排列的最少操作步数
#
# 解法1(T53% S10%): 在纸上试了n=8和n=6的流程，还是有一点规律的，但没有想到比直接模拟更好的办法，就直接开始写代码了。有一点小的创新是：因为每轮模拟，位置的移动都是固定的，也就是说不需要每次判断i的奇偶再移动，可以直接把每个下标移动的位置提前算好存下来。然后就是模拟遍历，终止条件是如果arr的第一位1如果归位了，则其他位置也一定归位了（通过在纸上模拟的不完全证明结论）
#

# @lc code=start
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n<=3: return 1

        move = []
        for i in range(n):
            if i%2==0:
                move.append(i//2)
            else:
                move.append(n//2+(i-1)//2)

        arr = [_ for _ in range(n)]
        cnt = 0
        while True:
            newarr = [0 for _ in range(n)]
            for j in range(n):
                newarr[j] = arr[move[j]]
            arr = newarr
            cnt += 1
            if arr[1] == 1:
                break
        return cnt
# @lc code=end

