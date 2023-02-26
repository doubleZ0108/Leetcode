#
# @lc app=leetcode.cn id=1255 lang=python3
#
# [1255] 得分最高的单词集合
#
# 解法1(T84% S46%)：题目看着挺复杂，但越是条件多的题其实对于算法本身的要求就没有那么苛刻，从小到大的事情也大都是这样，看了题目的取值范围，这么小的数胡乱做都不会超时的，因此本题可以看作是到纯业务逻辑题。本质上我们就是选一些words中的元素，让他们的得分最高，但words中的词必须能由letters构建出，由于题目数值小，我们不妨模拟出所有可能的words组合，既然是想找到所有可行解，又是一个数组的结构，那不妨通过深搜dfs来做。首先我们先统计下letters中每个字母出现的频次（利用Counter()或哈希表），然后进入递归的dfs函数，如果当前的单词的字母统计没超过letters的统计，那这个词可以选，统计中减去这个单词中所有字母的频次，进行下一重递归；另一种可能是当前这个数不选直接进入下一重递归。所有可能的结果都找到之后，再一次遍历计算并找到得分最高的结果就可以了。

# @lc code=start
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        cands = []
        
        def deepin(i, parts, cnt_remain):
            if i >= len(words): 
                cands.append(parts)
                return
            cnt_ = {}
            for key, val in cnt_remain.items():
                cnt_[key] = val
            flag = True
            for ch in words[i]:
                if ch in cnt_ and cnt_[ch]>0:
                    cnt_[ch] -= 1
                else:
                    flag = False
                    break
            if flag:
                deepin(i+1, parts + [words[i]], cnt_)
            deepin(i+1, parts, cnt_remain)
        
        deepin(0, [], Counter(letters))
        
        def cal(strs):
            cnt = 0
            for s in strs:
                for ch in s:
                    cnt += score[ord(ch)-ord('a')]
            return cnt
        
        return max(list(map(lambda x: cal(x), cands)))
        
# @lc code=end

