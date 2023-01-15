/*
 * @lc app=leetcode.cn id=208 lang=javascript
 *
 * [208] 实现 Trie (前缀树)
 */

// @lc code=start
var TrieNode = function(val, isword, nextDict) {
    this.val = (val==undefined? "" : val);
    this.isword = (isword==undefined? false : isword);
    this.nextDict = new Map();
};

var Trie = function() {
    this.root = new TrieNode();
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    var move = this.root;
    for (var ch of word) {
        if (!move.nextDict.has(ch)) {
            move.nextDict.set(ch, new TrieNode(ch));
        }
        move = move.nextDict.get(ch);
    }
    move.isword = true;
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    var move = this.root;
    for (var ch of word) {
        if (!move.nextDict.has(ch)) {
            return false;
        } else {
            move = move.nextDict.get(ch);
        }
    }
    return move.isword;
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    var move = this.root;
    for (var ch of prefix) {
        if (!move.nextDict.has(ch)) {
            return false;
        } else {
            move = move.nextDict.get(ch);
        }
    }
    return true;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
// @lc code=end

