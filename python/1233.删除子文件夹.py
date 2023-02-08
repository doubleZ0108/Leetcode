#
# @lc app=leetcode.cn id=1233 lang=python3
#
# [1233] 删除子文件夹
#
# 解法1(T37% S76%)：首先将文件夹排序，先考虑完更短的路径，这样长的路径才可能找到上层文件夹，使用集合（哈希表）维护结果，对于每条路径不断的剔除掉最右侧的`/` 之后的路径，如果在集合中已经存在则证明是别人的子文件夹
#     python中剔除最右侧的元素可以结合数组切片`[:]`和右侧查找`rindex()`

# @lc code=start
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = set()
        for path in folder:
            tmp = path
            flag = True
            while tmp and tmp[0]=="/":
                tmp = tmp[:tmp.rindex("/")]
                if tmp in res:
                    flag = False
                    break
            if flag:
                res.add(path)
        return list(res)
# @lc code=end

