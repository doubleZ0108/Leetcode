/*
 * @lc app=leetcode.cn id=155 lang=javascript
 *
 * [155] 最小栈
 */

// @lc code=start
var MinStack = function() {
    this.data = [];
    this.min = Infinity;
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.data.push(val);
    if (val < this.min) {
        this.min = val;
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    if (this.top() == this.min) {
        var tmp = Infinity;
        for (var i=0; i<this.data.length-1; i++) {
            if (this.data[i] < tmp) {
                tmp = this.data[i];
            }
        }
        this.min = tmp;
    }
    return this.data.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.data[this.data.length-1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.min;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
// @lc code=end

