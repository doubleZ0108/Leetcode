#
# @lc app=leetcode.cn id=1326 lang=python3
#
# [1326] 灌溉花园的最少水龙头数目
#
# 解法1(T100% S75%)：滑窗，看到区间的问题马上想到了滑窗。我们通过一个滑窗维护哪些水龙头选，依次循环每个不为空的水龙头，如果当前水龙头能往右喷的更远，则应该把这个水龙头选上，但是同样的应该从滑窗中弹出一些“旧”的：1）如果当前的水龙头left≤0那就是说这一个人就能一手掌握了，那所有之前的内容都可以被弹出了；2）还有一种情况是如果 倒数第二个元素+当前元素 能覆盖现在的区域那倒数第一个就冗余可以弹出了。将滑窗维护完为了保险起见再依次遍历判断能否覆盖完整的区间（不能相信滑窗内部一定能完整覆盖区间，不信你试试第36个测试样例，虽然第一遍做的时候就直接写了这块的逻辑，但是想看看是否有这样卡的紧的例子，算法题如果是一重循环的话还是保险点再循环一边比较好）
#     通过一个大例子更好明白，我们都知道肯定上来就要选3号位置的这个黄色的5，因为它往左能到头往右能伸展很远；我们接着往后走，比如走到9号位置这个红色的4，如果不看后面的序列它肯定要选上的，因为它能扩展到13这么远，我们不妨先加入滑窗；等我们走到绿色的3时发现右侧能延申到15>13，我肯定要选上这个绿色的3，但是发现绿色的左端点9可以正好跟之前黄色的8连上，也就是说不需要红色的4也能覆盖区间，那就把4弹出滑窗

# @lc code=start
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        win = []
        for i in range(len(ranges)):
            if ranges[i]!=0:
                left, right = i-ranges[i], i+ranges[i]

                if len(win) == 0:
                    win.append((left, right))
                    continue
                
                if right>win[-1][1]:
                    while win and left<=0:  # 如果我这段左端点能覆盖之前所有，那我一个人就够了
                        win.pop()
                    while len(win)>=2 and win[-2][1]>left-1:  # 当前最后一个冗余了
                        win.pop()

                    win.append((left, right))

                if win and win[0][0]<=0 and win[-1][1]>=n:
                    break
                
        if not win: return -1

        left, right = win[0]
        for i in range(1, len(win)):
            if win[i][0] > right:
                return -1
            left, right = min(left, win[i][0]), max(right, win[i][1])

        if left<=0 and right>=n:
            return len(win)
        else:
            return -1
# @lc code=end

