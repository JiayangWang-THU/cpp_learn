/*
 * @lc app=leetcode id=169 lang=cpp
 *
 * [169] Majority Element
 */

// @lc code=start
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> count_map;
        for (int n : nums){
            count_map[n]++;
            if (count_map[n] > nums.size()/2){
                return n;
            }
        }
        return -1;
    }
};
// @lc code=end

