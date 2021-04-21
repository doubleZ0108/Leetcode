/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> save_nums = nums;

        sort(nums.begin(), nums.end());
        for(int i=0,j=nums.size()-1;i<j;){
            int thisnum = nums[i] + nums[j];
            if(thisnum < target){
                i++;
            } else if(thisnum > target) {
                j--;
            } else {
                vector<int> result;
                for(int k=0;k<save_nums.size();++k){
                    if(save_nums[k] == nums[i] || save_nums[k] == nums[j]){
                        result.push_back(k);
                    }
                }
                return result;
            }
        }
        vector<int> empty;
        return empty;
    }
};
// @lc code=end

