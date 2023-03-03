#
# @lc app=leetcode.cn id=1487 lang=python3
#
# [1487] 保证文件名唯一
#
# 解法1(T11% S77%)：是一道非常实际的问题，跟win系统下的文件夹创建规则很像，主要要看懂示例2和示例5，同时不要把问题想的太复杂。对于输入的names我们肯定是一个一个看，如果当前的name之前没有过那没啥说的直接原封不动，如果之前有了才要在后面加一个括号后缀，所以我们得有一个数据结构把之前见过的存下来，集合或者哈希表就可以，因为我们可能反反复复的要查找，用集合查找起来速度只有$O(1)$。因此如果当前name在集合中没有我就原封不动放入结果并且添加进集合，如果之前存在了，我就开始不断模拟，在后面给他加上一个数字，指导找到加上这个数字括号后在集合中没有，那这个就是所谓的最小正整数

# @lc code=start
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        memo = set()
        res = []
        for name in names:
            if name not in memo:
                memo.add(name)
                res.append(name)
            else:
                k = 1
                while True:
                    tmp = f"{name}({k})"
                    if tmp not in memo:
                        memo.add(tmp)
                        res.append(tmp)
                        break
                    k += 1
        return res

# @lc code=end

