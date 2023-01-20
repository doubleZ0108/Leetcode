#
# @lc app=leetcode.cn id=1817 lang=python3
#
# [1817] 查找用户活跃分钟数
#
# 解法1(T45% S31%)：注意题目给出的几个例子非常容易让人理解错题目，可以先看如下这个例子。题目的意思是logs中每个元素是指id的用户在那一分钟用了软件，而不是指用了软件time分钟，首先要把这层逻辑想明白。解题而言，首先我们要统计每个用户都活跃了几分钟，然后再统计总长每个时间的用户有多少个。
# 因为用户可能id很大而logs数目很少，因此开辟个全长数组是不合理的，还是用哈希表来做比较好，具体而言key为用户id，而val为一个`set()`用于保存不重复的用户活跃时间点，统计完之后，每个用户的set的长度就是他活跃的时长了，我们再一遍哈希表统计每个总时长都有多少用户，然后再转换为结果的数组格式即可

# @lc code=start
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = {}
        for uid, time in logs:
            if uid not in users:
                users[uid] = set([time])
            else:
                users[uid].add(time)

        userscnt = Counter(map(lambda x: len(x), users.values()))
        res = [0 for _ in range(k)]
        for idx_, cnt in userscnt.items():
            res[idx_-1] = cnt
        return res
# @lc code=end

