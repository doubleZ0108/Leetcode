#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#
# 解法1(T38% S48%)：因为相同的字符要统计多变所以还是很绕的，如果不同字符只算一遍那直接将每个字符串转为集合再通过集合的交集运算跑一遍就行了，但考虑到相同字符都要考虑因此只能通过哈希表统计每个字符出现的次数，如果第一个哈希表的某个key在第i个哈希表中不存在则直接删除这个key；如果在则将val设为二者的最小值，循环一次所有字符串就好
#     Python `Counter()`中删除某个key对应的元素语法为 `del cnt[key]`

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mincnt = Counter(words[0])
        for i in range(1, len(words)):
            cnt = Counter(words[i])
            for key in mincnt.keys():
                if key not in cnt:
                    del mincnt[key]
                else:
                    mincnt[key] = min(mincnt[key], cnt[key])
        
        res = []
        for key, val in mincnt.items():
            res += [key for _ in range(val)]
        return res
# @lc code=end

