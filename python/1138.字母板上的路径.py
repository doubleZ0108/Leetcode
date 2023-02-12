#
# @lc app=leetcode.cn id=1138 lang=python3
#
# [1138] 字母板上的路径
#
# 解法1(超时 51/61)：深搜
# 解法2(T6% S46%)：广搜。这道题可以看做有一重循环的路径搜索问题，依次从上一个字母位置到下一个字母位置，但注意我们只需要找到一条最近的路径，而不需要找到所有路，所以解法1的深搜肯定会超时的，改为队列维护的广搜就好啦。内层的广搜跟普通的BFS区别在于，除了要保存位置信息还要保存上一步是怎么走的，也就是UDLR信息，同时Z字母的位置也比较特殊这也是之前BFS没见过的特例。总体而言本题是比较经典的搜索问题不过变种变的还是蛮有趣的
#     改进：由于字母表是有序的，因此很多搜索都是没必要的，比如要寻找的字母比当前所在位置字母更大，那肯定只有向下找，还有字母间存在一些数字关系，比如两个字母的差是5那他们一定是上下邻居关系，这些字母表的特殊性质作为条件可以加速

# @lc code=start
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        res = ""
        i, j = 0, 0
        for to in target:
            visited = set()
            queue = [(i, j, "")]
            while queue:
                x, y, parts = queue.pop(0)
                if board[x][y] == to:
                    res += parts + "!"
                    i, j = x, y
                    break
                visited.add(board[x][y])
                
                for dx, dy in [(x+1,y), (x-1,y), (x,y-1), (x,y+1)]:
                    if dx<0 or dy<0 or dx>5 or dy>4:
                        continue
                    if dx==5 and dy!=0:
                        continue
                    if board[dx][dy] in visited:
                        continue
                    if dx == x+1:
                        queue.append((dx, dy, parts+"D"))
                    if dx == x-1:
                        queue.append((dx, dy, parts+"U"))
                    if dy == y+1:
                        queue.append((dx, dy, parts+"R"))
                    if dy == y-1:
                        queue.append((dx, dy, parts+"L"))
        return res
# @lc code=end

