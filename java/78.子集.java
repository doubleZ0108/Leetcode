/*
 * @lc app=leetcode.cn id=78 lang=java
 *
 * [78] 子集
 */

// @lc code=start
class Solution {
    public HashSet<List<Integer>> res = new HashSet<List<Integer>>();
    public int length;
    public int[] nums;

    public void deepin(int index, List<Integer> parts) {
        if (index >= length) {
            res.add(parts);
            return;
        }
        List<Integer> parts_ = new ArrayList<>();
        List<Integer> n = new ArrayList<>(Arrays.asList(this.nums[index]));
        parts_.addAll(parts);
        parts_.addAll(n);
        deepin(index+1, parts_);
        deepin(index+1, parts);
    }

    public List<List<Integer>> subsets(int[] nums) {
        this.length = nums.length;
        this.nums = nums;
        deepin(0, new ArrayList());
        return new ArrayList(res);
    }
}
// @lc code=end

