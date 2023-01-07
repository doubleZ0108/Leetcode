/*
 * @lc app=leetcode.cn id=1658 lang=javascript
 *
 * [1658] 将 x 减到 0 的最小操作数
 * 
 * 解法1(超时 12/94)：回溯，首先一想肯定会超时，因为回溯本质就是一点一点试探，加一位进来完整尝试一遍，如果最终不行则跳过这位再试下一位，只能说是一种写法比较优雅的暴力枚举法。但还是说下回溯的设计：递归函数的参数为双支针ij划定范围，val用于判断递归终止；如果val==0了，则只需要0步就可以满足题设条件；如果双支针交叉了则证明此时无解，返回-1；模拟删除左侧元素，左指针+1并且val-nums[i]，这本身就是一步操作，因此调用递归后+1；同理，右侧也一样。最终要进行判断是否某侧返回结果有-1，否则返回最小值
    - 改进1: 递归时如果i元素和j元素都比当前val大，则一定没有解，直接返回-1
    - 改进2: 如果有一边的元素太大了，则这边就直接舍弃了，只递归另一边，极端情况如改进1
    - 改进3: 如果i和j元素相等，则只递归i就可以了，j这边也可以舍弃
*
* 解法2(JS T47% S35%)：因为最终总归是要在左边排除一些元素，右面也排除一些元素，换个视角也就相当于盖住数组中间一些元素，让外面那些元素的和为x，也就相当于让盖住的和为sum-x，而且中间盖住的部分一定是连续的，这就很容易想到了滑动窗口（我怎么没想到¿）
    具体而言，通过left和right指针刻画滑窗的左右端点，初始时滑窗内部为首元素，开始循环，如果滑窗内的元素和==sum-x，则证明此时滑窗外的元素构成了一个可行解，注意只是可行解并不一定是最优解，因此记录下最小值，right继续往后遍历；如果滑窗内总和太小了，则right向右移动一位，可以盖住更多的元素；如果滑窗内太大了，则left向右移动一位。还有一种特殊情况，即left还在初始位置，但此时滑窗内和==x，也就意味着开头这些元素正好组成了可行解，那也要记录最小值，right继续往后遍历
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
// 解法2
var minOperations = function(nums, x) {
    if (nums.length == 1) { return nums[0]==x ? 1 : -1; }
    if (nums[0]>x && nums[nums.length-1]>x) { return -1; }

    var sum = _.sum(nums);
    if (sum < x) { return -1; }

    var left=0, right=1, winsum = nums[0];
    var minlen = nums.length+1;
    while (right<nums.length) {
        if (left==0 && winsum==x) { 
            minlen = Math.min(minlen, right);
            winsum += nums[right];
            right++;
        } else if (sum - winsum == x) {
            minlen = Math.min(minlen, nums.length - (right - left));
            winsum += nums[right];
            right++;
        } else if (sum - x > winsum) {
            winsum += nums[right];
            right++;
        } else {
            winsum -= nums[left];
            left++;
        }
    }

    return minlen < nums.length+1 ? minlen : -1;
};

// 解法1 超时
var minOperations = function(nums, x) {
    if (nums.length == 1) { return nums[0]==x ? 1 : -1; }
    if (nums[0]>x && nums[nums.length-1]>x) { return -1; }
    if (nums.reduce((a,b) => a+b) < x) { return -1; }

    var operate = function(i, j, val) {
        if (val == 0) { return 0; }
        if (i > j) { return -1; }

        var left = operate(i+1, j, val-nums[i]) + 1;
        var right = operate(i, j-1, val-nums[j]) + 1;

        if (left==-1 && right==-1) { return -1; }
        else if (left == -1) { return right; }
        else if (right == -1) { return left; }
        else { return Math.min(left, right); }
    };

    var res = operate(0, nums.length-1, x);

    return res;
};

// 解法1 改进1 2 3
var minOperations = function(nums, x) {
    if (nums.length == 1) { return nums[0]==x ? 1 : -1; }
    if (nums[0]>x && nums[nums.length-1]>x) { return -1; }
    if (nums.reduce((a,b) => a+b) < x) { return -1; }

    var operate = function(i, j, val) {
        if (val == 0) { return 0; }
        if (nums[i]>val && nums[j]>val) { return -1; }
        if (i > j) { return -1; }

        var left, right;
        if (nums[i] <= val) {
            left = operate(i+1, j, val-nums[i]) + 1;
        }
        if (nums[i]!=nums[j] && nums[j] <= val) {
            right = operate(i, j-1, val-nums[j]) + 1;
        }

        if (!left) {
            return right>0 ? right : -1;
        } else if (!right) {
            return left>0 ? left : -1;
        } else {
            if (left<=0 && right<=0) { return -1; }
            else if (left <= 0) { return right; }
            else if (right <= 0) { return left; }
            else { return Math.min(left, right); }
        }

    };

    var res = operate(0, nums.length-1, x);

    return res;
};
// @lc code=end

