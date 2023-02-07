/*
 * @lc app=leetcode.cn id=133 lang=javascript
 *
 * [133] 克隆图
 * 
 * 解法1(T81% S99%)：非常有趣的一道题，邻接表表示的图的复制，考虑到python深浅指针不太行所以用js这种有new语法的语言实现。想要复制一个图，必然要遍历原图的每个节点，遍历算法是经典的队列+visited集合的图标配，由于js集合查找速度很慢所以一般直接开一个全长的标志位数组。而如何复制呢，因为题目中图的节点值和下标是一一对应的，那不妨用一个数组保存图中所有节点，初始时只填上节点的值即它的下标，而在遍历图的时候将每个节点的neighbors都填入到新图中该节点的neighbors，代码写起来很有趣味
 */

// @lc code=start
/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
    if (!node) { return null; }
    if (node.neighbors.length==0) { return new Node(node.val, new Array()); }

    var visited = new Array(101).fill(false);
    var queue = [node];
    visited[node.val] = true;
    var graph = new Array(101)
    for (var i=1; i<graph.length; i++) {
        graph[i] = new Node(i, new Array());
    }

    while (queue.length) {
        var n = queue.shift();

        for (var neighbor of n.neighbors) {
            graph[n.val].neighbors.push(graph[neighbor.val]);
            if (!visited[neighbor.val]) {
                queue.push(neighbor);
                visited[neighbor.val] = true;
            }
        }
    }
    return graph[node.val];
};
// @lc code=end

