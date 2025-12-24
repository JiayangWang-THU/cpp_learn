/*
 * @lc app=leetcode id=217 lang=cpp
 *
 * [217] Contains Duplicate
 */

// @lc code=start
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> cnt;
        for (int x : nums){
            cnt[x]++;
            if (cnt[x]>1)
                return true;
        }
        return false;
    }
};
// @lc code=end

