/*
 * @lc app=leetcode.cn id=232 lang=javascript
 *
 * [232] 用栈实现队列
 */

// @lc code=start
var MyQueue = function() {
    this.leftstack = [];
    this.rightstack = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    this.leftstack.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    this.peek();
    return this.rightstack.pop();
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    if (this.rightstack.length == 0) {
        while (this.leftstack.length > 0) {
            this.rightstack.push(this.leftstack.pop());
        }
    }
    return this.rightstack[this.rightstack.length-1];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    return this.leftstack.length==0 && this.rightstack.length==0;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
// @lc code=end

