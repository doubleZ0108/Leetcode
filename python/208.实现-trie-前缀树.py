#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#
# 解法1(T76% S67%): 是数据结构设计的题。对于前缀树（字典树）中每个节点`TrieNode`保存的是children节点，可以通过一个字典实现，同时要设置一个flag标明当前节点是否为完整的单词，叶子节点保存的就是一个完整的单词但并不是所有单词都是叶
#   `insert()`：把每个字母都当作一个节点挂在上一个节点的children中，如果children中已经有了这个字符那就不用创建了直接使用就可以
#   `search()`：不断搜索children，如果最终停下来的flag是word，则证明找到了这个单词
#   `startsWith()`：跟search逻辑一样，只是不需要满足停下来的时候是单词，只要之前一直满足children中有各个字符就可以
#
#       为什么要设立flag标识是否为单词呢？比如第一次插入app，那一个左支树a-p-p；又插入apple，发现之前已经有a-p-p了，所以接着往后挂就可以a-p-p-l-e，但app也是一个单词，最后的p并不是叶节点

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children: return False
            node = node.children[c]
        return node.isWord


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children: return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

