/*
 * @lc app=leetcode id=219 lang=cpp
 *
 * [219] Contains Duplicate II
 */

// @lc code=start
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int,int> last_pos;
        for (int i=0;i<nums.size();i++){
            int x=nums[i];
            if (last_pos.count(x) && i - last_pos[x]<=k)
                return true;
            last_pos[x]=i;}
        return false;
        
    }
};
// @lc code=end

