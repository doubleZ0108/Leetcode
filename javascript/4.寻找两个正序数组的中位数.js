/*
 * @lc app=leetcode.cn id=4 lang=javascript
 *
 * [4] 寻找两个正序数组的中位数
 * 
 * 解法1: 最基础的想法肯定是引入一个新数组，把两个数组都放进来，然后排序，直接根据奇偶选中位数，但感觉肯定会超时或者爆显存
 * 
 * 解法2(T88% S30%): 因为题干强调了log的时间复杂度，所以肯定是二分查找的思想，通过两个指针分别指向两数组的开头，求解中位数本质上就是把前n/2-1个最小的数扔掉，这个思想可以很好的通过二分查找来实现，不过需要注意的是有可能一个数组很短而另一个很长，因此需要判断是否有指针已经到尾部，如果是的话只在另一个数组中移动就可以了。扔完n/2-1个数之后，根据原数组长度的奇偶性来选取中位数即可，一个小技巧，可以直接把之后的数组切片合并成一个数组然后讨论第0号和1号元素，这样省时方便又不用担心爆内存（因为至少有一半已经被排除掉了）
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    var flag = (nums1.length + nums2.length) % 2 == 0;   // 中位数是中间两个数的平均
    var midNum = Math.floor((nums1.length + nums2.length)/2);
    for (var i=0, j=0; i+j<(flag ? midNum-1 : midNum); ) {
        if (i == nums1.length) {
            j++;
            continue;
        } else if (j == nums2.length) {
            i++;
            continue;
        }

        if (nums1[i] < nums2[j]) {
            i++;
        } else {
            j++;
        }
    }

    var tmp = [...nums1.slice(i), ...nums2.slice(j)].sort((a,b)=>a-b);
    if (!flag) {
        return tmp[0];
    } else {
        
        return (tmp[0]+tmp[1]) / 2;
    }
};
// @lc code=end

