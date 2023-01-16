#
# @lc app=leetcode.cn id=1813 lang=python3
#
# [1813] 句子相似性 III
#
# 解法1(T19% S29%): 初始想法不难，主要都是针对特殊用例增增补补导致代码很冗杂。基础想法就是将字符串按照空格划分为数组，然后通过双指针来判断，如果两位相等则双指针都往后移，如果某位不一样了，则代表要在这里插入几个词才可能相等，所以长的串指针不断后移找到能匹配的，同时因为只能在一个位置插入，所以如果有第二次不匹配的话就可以直接返回False了。接下来是一些小点我们分别来看：
#     - 首先两个句子如果长度相等就可以提前判断了，此时二者只能相等（相似）或不相似
#     - 题目没说哪个串长，所以要提前交换一下
#     - 如果短串里有单词压根没在长串里出现，那肯定不相似；但注意不能只用issubset()来判断，不够严格，要通过哈希表判断出现频次，如下🌰(3)
#     - 这题烦就烦在🌰(1)(4)这种多匹配的，比如(1)，如果A跟长串第一个A匹配的话二者不相似，但如果跟第二个A匹配则二者相似，最终结果肯定还应该是相似，怎么克服这个问题呢？想到两点
#         1. 首先可以通过判断短串是否做为长串的头或者尾，比如(1)就可以通过这种方法解决，但要注意不能直接对原句子使用startswith()，因为🌰(2)，必须要是一个单词，而不是几个字母
#         2. 第二只能通过双指针从前遍历一次再从后向前遍历一次来实现了，虽然有点笨但总归能解决问题
# 
# 解法(T98% S35%): 同样是先分割字符串为数组再使用双指针，左指针从左到右将二者前面匹配的部分都跳过，右指针从右到左把二者后面匹配的部分都跳过，如果两指针完整的走过了短串，那就证明可以在短串中间插入一句话使得二者相等。比较麻烦的就是数组下标的处理，右指针可以利用python的属性从-1开始往前减，最终的判断条件为i-j-1==len(word2)。有一点需要注意如🌰(4)，由于左指针已经把AB都处理完了，因此右指针不能再重复处理BB，因此右指针要满足在左指针后面的部分循环，要为此添加一个循环的条件

# @lc code=start
class Solution:
    # 解法2
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) < len(sentence2): sentence1, sentence2 = sentence2, sentence1
        words1, words2 = sentence1.split(" "), sentence2.split(" ")

        i, j = 0, -1
        while i<len(words1) and i<len(words2) and words1[i]==words2[i]:
            i += 1
        while j>-len(words1)-1 and j>-len(words2)-1 and len(words2)+j+1>i and words1[j]==words2[j]:
            j -= 1
        return i-j-1 == len(words2)

    # 解法1
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) == len(sentence2): return sentence1==sentence2
        if len(sentence1) < len(sentence2): sentence1, sentence2 = sentence2, sentence1

        def similar(sentence1, sentence2):
            words1, words2 = sentence1.split(" "), sentence2.split(" ")
            freq1, freq2 = Counter(words1), Counter(words2)
            for key, val in freq2.items():
                if key not in freq1: return False
                if val>freq1[key]: return False
            if words1[:len(words2)] == words2 or words1[-len(words2):]==words2: return True

            i, j = 0, 0
            cnt = 0
            while i<len(words1) and j<len(words2):
                if words1[i] == words2[j]:
                    i += 1
                    j += 1
                    continue
                else:
                    cnt += 1
                    if cnt==1:
                        i += 1
                        while i<len(words1) and words1[i]!=words2[j]:
                            i += 1
                    if cnt>1:
                        return False

            if cnt==1:
                return i==len(words1)
            elif cnt==0:
                return True

        return similar(sentence1, sentence2) or similar(sentence1[::-1], sentence2[::-1])

Solution().areSentencesSimilar("a A b A", "A")
Solution().areSentencesSimilar("ByI BMyQIqce b bARkkMaABi vlR RLHhqjNzCN oXvyK zRXR q ff B yHS OD KkvJA P JdWksnH", "B")
Solution().areSentencesSimilar("A aA", "A A")
Solution().areSentencesSimilar("A B C D B B", "A B B")
# @lc code=end

