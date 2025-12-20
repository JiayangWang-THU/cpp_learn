/*
 * @lc app=leetcode id=35 lang=cpp
 *
 * [35] Search Insert Position
 */

// @lc code=start
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();
        int mid = 0;
        while(left < right){            
            mid = left + (right - left)/2;
            if(nums[mid]<target){
                left = mid + 1;
            }
            else
                right = mid;
        }
        return left;

    }
};
// @lc code=end

