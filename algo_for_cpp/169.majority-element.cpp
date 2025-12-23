/*
 * @lc app=leetcode id=169 lang=cpp
 *
 * [169] Majority Element
 */

// @lc code=start
class Solution {
public:
    int majorityElement(vector<int>& nums) {
     sort(nums.begin(), nums.end());
     return nums[nums.size()/2];
    }
};
// @lc code=end
//hash map
// class Solution {
// public:
//     int majorityElement(vector<int>& nums) {
//         unordered_map<int, int> count_map;
//         for (int n : nums){
//             count_map[n]++;
//             if (count_map[n] > nums.size()/2){
//                 return n;
//             }
//         }
//         return -1;
//     }
// };
// Boyer-Moore Voting Algorithm
//   int count = 0;
//        int candidate = 0;
//        for (int n : nums){
//             if(count == 0){
//                 candidate = n;
//             }
//             count += (n == candidate) ? 1 : -1;
//        }
//        return candidate;