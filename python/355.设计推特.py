#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#
# 解法1(T52% S14%)：题干描述的还是很清晰的，读完题发现主要有四个功能，直观来想要维护两个数据结构：1）推文池；2）朋友关系。对于所有推文因为之后需要按时间最近的顺序取出来因此想到通过优先队列维护加速后续查找，而对于关注者关系通过邻接表来存储就可以，具体来看通过哈希表来做，key设为userId，val设为集合存储所有关注者的Id方便后续查找
#     `init()`: 按照刚才描述的初始化一个优先队列和一个哈希表用来存储邻接表，需要注意优先队列要指定发文时间为排序依据，所以还需要一个全局时间戳记录每条推文发布的时间
#     `post()`: 根据时间戳将该用户的这条推文放入全局推文池就好（该实现主要把复杂度放在查找端，增数据端不处理关注者的逻辑）
#     `get()`: 我们从优先队列中时间最大的推文开始遍历，如果推文的userid是我自己或者我关注的人则加入结果中，当结果里有10条推文就可以终止查找了
#     `follow()`: 按照邻接表的方式将关注者关系加入全局数据结构中，当第一次设置某个人关注的人时创建一个key-val对，否则直接加入val的集合就好
#     `unfollow()`: 如果当前人曾经记录过朋友则从他关注的集合中把这个人移除
#
#     更进一步想微信朋友圈这么大的数据量肯定不会把所有人发的朋友圈都维护在一个池子里，所以本题只是一个十分navie的维护方式

# @lc code=start
from sortedcontainers import SortedList

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweets = SortedList(key=lambda x: x[-1])
        self.friends = {}


    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets.add((userId, tweetId, self.time))
        self.time += 1


    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(self.tweets)-1, -1, -1):
            userId_, tweetId_, _ = self.tweets[i]
            if userId_==userId or (userId in self.friends and userId_ in self.friends[userId]):
                res.append(tweetId_)
            if len(res) == 10:
                break
        return res


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.friends:
            self.friends[followerId] = set([followeeId])
        else:
            self.friends[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.friends:
            self.friends[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

