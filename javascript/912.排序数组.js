/*
 * @lc app=leetcode.cn id=912 lang=javascript
 *
 * [912] 排序数组
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[]}
 */
// 快排
var getPivot = function(nums, i, j) {
    var pivot = i;
    var left=i+1, right=j;
    while (left < right) {
        while (left < right && nums[left]<=nums[pivot]) {
            left++;
        }
        while (left < right && nums[right]>nums[pivot]) {
            right--;
        }
        if (left < right) {
            var tmp = nums[left];
            nums[left] = nums[right];
            nums[right] = tmp;
        }
    }
    if (nums[left] > nums[pivot]) {
        left--;
    }
    var tmp = nums[pivot];
    nums[pivot] = nums[left];
    nums[left] = tmp;
    return left;
};

var fastsort = function(nums, i, j) {
    if (i < j) {
        var pivot = getPivot(nums, i, j);
        fastsort(nums, i, pivot-1);
        fastsort(nums, pivot+1, j);
    }
};

var sortArray = function(nums) {
    nums.sort((a, b) => .5-Math.random());
    console.log(nums)
    fastsort(nums, 0, nums.length-1);
    return nums;
};

// 归并排序 自顶向下
var merge = function(arr1, arr2) {
    var res = [];
    var i=0, j=0;
    while (i<arr1.length && j<arr2.length) {
        if (arr1[i] <= arr2[j]) {
            res.push(arr1[i]);
            i++;
        } else {
            res.push(arr2[j]);
            j++;
        }
    }
    while (i<arr1.length) {
        res.push(arr1[i]);
        i++;
    }
    while (j < arr2.length) {
        res.push(arr2[j]);
        j++;
    }
    return res;
};


var mergesort = function(nums) {
    if (nums.length<=1) {
        return nums;
    }
    return merge(
        mergesort(nums.slice(0, Math.floor(nums.length/2))), 
        mergesort(nums.slice(Math.floor(nums.length/2)))
    );
};

var sortArray = function(nums) {
    return mergesort(nums);
};


// 插入排序
var insertSortArray = function(nums) {
    for (var i=1; i<nums.length; i++) {
        var j = i-1;
        var tmp = nums[i];
        while (j>-1 && tmp < nums[j]) {
            nums[j+1] = nums[j];
            j--;
        }
        nums[j+1] = tmp;
    }
    return nums;
};

// 选择排序
var selectSortArray = function(nums) {
    for (var i=0; i<nums.length-1; i++) {
        var minidx = i;
        for (var j=i+1; j<nums.length; j++) {
            if (nums[j] < nums[minidx]) {
                minidx = j;
            }
        }
        if (minidx != i) {
            var tmp = nums[minidx];
            nums[minidx] = nums[i];
            nums[i] = tmp;
        }
    }
    return nums;
};

// 冒泡排序
var bubbleSortArray = function(nums) {
    var change = false;
    for (var i=0; i<nums.length-1; i++) {
        change = false;
        for (var j=0; j<nums.length-i-1; j++) {
            if (nums[j] > nums[j+1]) {
                var tmp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = tmp;
                change = true;
            }
        }
        if (!change) { break; }
    }
    return nums;
};
// @lc code=end

