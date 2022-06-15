#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#
"""
解法1(超时)：看数据规模不大，本来想暴力解。首先将n个`(`和n个`)`加入到数组中，然后调用库函数`itertools.permutations()`进行全排列，并通过集合set()去重，最后再依次判断每个可能的组合是否合法，可以根据[20题](https://www.notion.so/20-16d4ba21305b4e02b772b2d1ab2af17d)的算法用栈来判断括号是否匹配

解法2(T60% S90%)：又是经典的深搜（携带参数递归），递归参数设定为`cur`代表当前做到的下标位置，`li`代表这一种情况的括号组成，还有两个参数`leftCount`和`rightCount`代表当前位置之前左右括号的数量。
    - 初始：`cur=1`（因为第一个必须是`(`），`li`的首元素是`(` 其余为空，`leftCount=1`，`rightCount=0`
    - 终止条件：如果`leftCount`或`rightCount`大于n则直接返回，当前解不可能（事实上只判断`leftCount`就好，`rightCount`不可能大于n）；如果`cur`指到最后位置2n了就可以将当前li转换为字符串加入结果中了
    - 递归：如果`leftCount>rightCount`，代表之前肯定有一个`(`，则可以把当前位置放一个`)`并递归；否则当前位置只能放`(`再递归
"""

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def gen(cur, li, leftCount, rightCount):
            if leftCount>n: return
            if cur == 2*n:
                res.append("".join(li))
                return
            if leftCount > rightCount:
                li[cur] = ')'
                gen(cur+1, li, leftCount, rightCount+1)
            li[cur] = '('
            gen(cur+1, li, leftCount+1, rightCount)     
            
        li = ['' for _ in range(2*n)]
        li[0] = '('
        gen(1, li, 1, 0)
        return res


    def otherSolution(self, n):
        # 解法1 超时
        def isValid(item):
            stack = []
            for s in item:
                if s == '(': stack.append(s)
                else:
                    if len(stack)<=0: return False
                    if stack.pop() != '(': return False
            return stack==[]

        li = []
        for i in range(n): 
            li.append('(')
            li.append(')')

        from itertools import permutations
        li = list(set(permutations(li)))

        res = []
        for item in li:
            if isValid(item): res.append("".join(item))
        return res
# @lc code=end

