/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i,j=0;
        for (i=0;i<nums.size();i++){
            for (j=i+1;j<nums.size();j++)
            {
                if (nums[i]+nums[j]==target)
                    return {i,j};
            }
        }
        return {};
    }
};
// @lc code=end

